#!/usr/bin/env python3
"""
Azure DevOps MCP Server Performance Benchmark

Measures performance of different API interactions
"""

import os
import time
from azure_devops_mcp import AzureDevOpsMCPServer
from dotenv import load_dotenv

def benchmark_method(method, *args, **kwargs):
    """
    Benchmark a method's performance
    """
    start_time = time.time()
    result = method(*args, **kwargs)
    end_time = time.time()
    
    return {
        'result': result,
        'execution_time': end_time - start_time
    }

def run_performance_benchmark(server):
    """
    Run comprehensive performance benchmarks
    """
    print("🚀 Azure DevOps MCP Server Performance Benchmark 🚀")
    print("================================================")
    
    # Get the first project for benchmarking
    projects = server.list_projects()
    if not projects:
        print("No projects found for benchmarking")
        return
    
    project_name = projects[0]['name']
    
    # Benchmark different methods
    benchmarks = {
        'List Projects': lambda: server.list_projects(),
        'List Repositories': lambda: server.list_repositories(project_name),
        'Get Work Items': lambda: server.get_work_items(project_name),
        'Get Team Members': lambda: server.get_team_members(project_name),
        'Get Build Definitions': lambda: server.get_build_definitions(project_name)
    }
    
    results = {}
    for name, method in benchmarks.items():
        print(f"\nBenchmarking: {name}")
        benchmark = benchmark_method(method)
        
        results[name] = {
            'execution_time': benchmark['execution_time'],
            'item_count': len(benchmark['result']) if isinstance(benchmark['result'], list) else 0
        }
        
        print(f"  Execution Time: {results[name]['execution_time']:.4f} seconds")
        print(f"  Items Retrieved: {results[name]['item_count']}")
    
    # Summary
    print("\n📊 Performance Summary:")
    for method, stats in results.items():
        print(f"{method}: {stats['execution_time']:.4f} sec ({stats['item_count']} items)")

def main():
    """
    Main execution function
    """
    load_dotenv()
    
    # Retrieve credentials from environment
    organization = os.getenv('AZURE_DEVOPS_ORG')
    pat = os.getenv('AZURE_DEVOPS_PAT')
    
    if not organization or not pat:
        print("Error: AZURE_DEVOPS_ORG and AZURE_DEVOPS_PAT must be set")
        return
    
    server = AzureDevOpsMCPServer(organization, pat)
    run_performance_benchmark(server)

if __name__ == '__main__':
    main()
