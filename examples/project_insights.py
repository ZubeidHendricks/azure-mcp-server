#!/usr/bin/env python3
"""
Azure DevOps Project Insights Script

This script demonstrates comprehensive project analysis 
using the Azure DevOps MCP Server.
"""

import os
from azure_devops_mcp import AzureDevOpsMCPServer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_project_insights(organization, pat):
    """
    Generate detailed insights for an Azure DevOps project
    """
    # Initialize the server
    server = AzureDevOpsMCPServer(organization, pat)
    
    # Retrieve projects
    projects = server.list_projects()
    
    print("🔍 Azure DevOps Project Insights 🔍")
    print("====================================")
    
    for project in projects:
        print(f"\nProject: {project['name']}")
        print(f"ID: {project['id']}")
        print(f"State: {project['state']}")
        
        # Repositories
        repos = server.list_repositories(project['name'])
        print(f"Repositories: {len(repos)}")
        for repo in repos:
            print(f"  - {repo['name']} (Default Branch: {repo.get('default_branch', 'N/A')})")
        
        # Work Items
        work_items = server.get_work_items(project['name'])
        print(f"Total Work Items: {len(work_items)}")
        
        # Work Item Summary
        status_summary = {}
        for item in work_items:
            status = item['state']
            status_summary[status] = status_summary.get(status, 0) + 1
        
        print("Work Item Status:")
        for status, count in status_summary.items():
            print(f"  - {status}: {count}")
        
        # Team Members
        team_members = server.get_team_members(project['name'])
        print(f"Team Members: {len(team_members)}")
        
        # Build Definitions
        build_defs = server.get_build_definitions(project['name'])
        print(f"Build Definitions: {len(build_defs)}")

def main():
    """
    Main execution function
    """
    # Retrieve credentials from environment
    organization = os.getenv('AZURE_DEVOPS_ORG')
    pat = os.getenv('AZURE_DEVOPS_PAT')
    
    if not organization or not pat:
        print("Error: AZURE_DEVOPS_ORG and AZURE_DEVOPS_PAT must be set")
        return
    
    get_project_insights(organization, pat)

if __name__ == '__main__':
    main()
