import os
import pytest
from azure_devops_mcp.server import AzureDevOpsMCPServer

# You would replace these with your actual test credentials
ORG = os.getenv('AZURE_DEVOPS_ORG', 'test-org')
PAT = os.getenv('AZURE_DEVOPS_PAT', 'test-pat')

@pytest.fixture
def azure_devops_server():
    return AzureDevOpsMCPServer(ORG, PAT)

def test_list_projects(azure_devops_server):
    """Test retrieving projects"""
    projects = azure_devops_server.list_projects()
    assert isinstance(projects, list)
    assert len(projects) > 0

def test_list_repositories(azure_devops_server):
    """Test retrieving repositories"""
    projects = azure_devops_server.list_projects()
    if projects:
        project_name = projects[0]['name']
        repos = azure_devops_server.list_repositories(project_name)
        assert isinstance(repos, list)

def test_get_work_items(azure_devops_server):
    """Test retrieving work items"""
    projects = azure_devops_server.list_projects()
    if projects:
        project_name = projects[0]['name']
        work_items = azure_devops_server.get_work_items(project_name)
        assert isinstance(work_items, list)

def test_get_build_definitions(azure_devops_server):
    """Test retrieving build definitions"""
    projects = azure_devops_server.list_projects()
    if projects:
        project_name = projects[0]['name']
        build_defs = azure_devops_server.get_build_definitions(project_name)
        assert isinstance(build_defs, list)

def test_get_team_members(azure_devops_server):
    """Test retrieving team members"""
    projects = azure_devops_server.list_projects()
    if projects:
        project_name = projects[0]['name']
        team_members = azure_devops_server.get_team_members(project_name)
        assert isinstance(team_members, list)
