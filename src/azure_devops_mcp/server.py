import os
import base64
from typing import Dict, Any, List, Optional
import requests
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

class AzureDevOpsMCPServer:
    def __init__(self, organization: str, pat: str):
        """
        Initialize Azure DevOps MCP Server
        
        :param organization: Azure DevOps organization name
        :param pat: Personal Access Token
        """
        self.organization = organization
        self.pat = pat
        self.base_url = f'https://dev.azure.com/{organization}'
        
        # Azure DevOps client setup
        credentials = BasicAuthentication('', pat)
        self.connection = Connection(base_url=self.base_url, creds=credentials)

    def list_projects(self) -> List[Dict[str, Any]]:
        """
        List all projects in the organization
        """
        try:
            core_client = self.connection.clients.get_core_client()
            projects = core_client.get_projects()
            return [
                {
                    'id': project.id,
                    'name': project.name,
                    'description': project.description or '',
                    'url': project.url,
                    'state': project.state
                } for project in projects
            ]
        except Exception as e:
            print(f"Error listing projects: {e}")
            return []

    def list_repositories(self, project_name: str) -> List[Dict[str, Any]]:
        """
        List repositories in a project
        
        :param project_name: Name of the project
        """
        try:
            git_client = self.connection.clients.get_git_client()
            repos = git_client.get_repositories(project_name)
            return [
                {
                    'id': repo.id,
                    'name': repo.name,
                    'url': repo.remote_url,
                    'project_name': repo.project.name,
                    'default_branch': repo.default_branch
                } for repo in repos
            ]
        except Exception as e:
            print(f"Error listing repositories: {e}")
            return []

    def create_pull_request(self, 
                             project_name: str, 
                             repo_name: str, 
                             source_branch: str, 
                             target_branch: str, 
                             title: str, 
                             description: str) -> Dict[str, Any]:
        """
        Create a new Pull Request
        
        :param project_name: Name of the project
        :param repo_name: Repository name
        :param source_branch: Source branch name
        :param target_branch: Target branch name
        :param title: Pull Request title
        :param description: Pull Request description
        """
        try:
            git_client = self.connection.clients.get_git_client()
            
            # Find the repository
            repo = git_client.get_repository(repo_name, project_name)
            
            # Create pull request object
            pull_request = {
                'sourceRefName': f'refs/heads/{source_branch}',
                'targetRefName': f'refs/heads/{target_branch}',
                'title': title,
                'description': description
            }
            
            # Create the pull request
            created_pr = git_client.create_pull_request(pull_request, repo.id)
            
            return {
                'id': created_pr.pull_request_id,
                'title': created_pr.title,
                'description': created_pr.description,
                'status': created_pr.status,
                'url': created_pr.url
            }
        except Exception as e:
            print(f"Error creating pull request: {e}")
            return {}

    def get_work_items(self, 
                        project_name: str, 
                        work_item_type: Optional[str] = None, 
                        state: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve work items from a project with optional filtering
        
        :param project_name: Name of the project
        :param work_item_type: Optional filter for work item type (e.g., 'Task', 'Bug')
        :param state: Optional filter for work item state
        """
        try:
            wit_client = self.connection.clients.get_work_item_tracking_client()
            
            # Build WIQL query with optional filters
            query_parts = [f"SELECT [System.Id], [System.Title], [System.State], [System.WorkItemType] FROM WorkItems WHERE [System.TeamProject] = '{project_name}'"]
            
            if work_item_type:
                query_parts.append(f"AND [System.WorkItemType] = '{work_item_type}'")
            
            if state:
                query_parts.append(f"AND [System.State] = '{state}'")
            
            query = " ".join(query_parts)
            
            # Run the query
            wiql = wit_client.query_by_wiql(query, project_name)
            
            # Get details for each work item
            work_items = []
            for item in wiql.work_items:
                work_item = wit_client.get_work_item(item.id)
                work_items.append({
                    'id': work_item.id,
                    'title': work_item.fields.get('System.Title', ''),
                    'state': work_item.fields.get('System.State', ''),
                    'type': work_item.fields.get('System.WorkItemType', ''),
                    'assigned_to': work_item.fields.get('System.AssignedTo', {}).get('displayName', 'Unassigned')
                })
            
            return work_items
        except Exception as e:
            print(f"Error retrieving work items: {e}")
            return []

    def get_build_definitions(self, project_name: str) -> List[Dict[str, Any]]:
        """
        Retrieve build definitions for a project
        
        :param project_name: Name of the project
        """
        try:
            build_client = self.connection.clients.get_build_client()
            definitions = build_client.get_definitions(project_name)
            
            return [
                {
                    'id': definition.id,
                    'name': definition.name,
                    'repository': {
                        'name': definition.repository.name if definition.repository else 'N/A',
                        'type': definition.repository.type if definition.repository else 'N/A'
                    },
                    'queue_status': definition.queue_status,
                    'type': definition.type
                } for definition in definitions
            ]
        except Exception as e:
            print(f"Error retrieving build definitions: {e}")
            return []

    def get_team_members(self, project_name: str, team_name: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve team members for a project
        
        :param project_name: Name of the project
        :param team_name: Optional specific team name
        """
        try:
            core_client = self.connection.clients.get_core_client()
            
            # If no team name is provided, get all teams
            if not team_name:
                teams = core_client.get_teams(project_name)
            else:
                teams = [core_client.get_team(project_name, team_name)]
            
            team_members = []
            for team in teams:
                members = core_client.get_team_members(project_name, team.id)
                team_members.extend([
                    {
                        'id': member.id,
                        'display_name': member.display_name,
                        'unique_name': member.unique_name,
                        'team_name': team.name
                    } for member in members
                ])
            
            return team_members
        except Exception as e:
            print(f"Error retrieving team members: {e}")
            return []

# Example usage for context
if __name__ == '__main__':
    # Replace placeholders with actual values
    server = AzureDevOpsMCPServer('your-org', 'your-pat')
    
    # Example method calls
    projects = server.list_projects()
    if projects:
        project_name = projects[0]['name']
        
        # Retrieve repositories
        repos = server.list_repositories(project_name)
        print("Repositories:", repos)
        
        # Retrieve work items
        work_items = server.get_work_items(project_name)
        print("Work Items:", work_items)
        
        # Retrieve build definitions
        build_defs = server.get_build_definitions(project_name)
        print("Build Definitions:", build_defs)
        
        # Retrieve team members
        team_members = server.get_team_members(project_name)
        print("Team Members:", team_members)
