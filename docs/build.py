#!/usr/bin/env python3
"""
Documentation build script for Azure DevOps MCP Server
"""

import os
import subprocess
import sys

def build_documentation():
    """
    Build Sphinx documentation
    """
    # Ensure we're in the docs directory
    docs_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(docs_dir)

    # Create build directory if it doesn't exist
    build_dir = os.path.join(docs_dir, '_build')
    os.makedirs(build_dir, exist_ok=True)

    # Run Sphinx build
    try:
        subprocess.run([
            'sphinx-build', 
            '-b', 'html',  # Build HTML documentation
            '.',           # Source directory
            '_build/html' # Output directory
        ], check=True)
        
        print("Documentation built successfully!")
        print(f"Open {os.path.join(build_dir, 'html', 'index.html')} to view")
    except subprocess.CalledProcessError as e:
        print(f"Documentation build failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_documentation()
