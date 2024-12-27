Welcome to Azure DevOps MCP Server's Documentation
================================================

.. image:: https://img.shields.io/pypi/v/azure-devops-mcp-server.svg
   :target: https://pypi.org/project/azure-devops-mcp-server/

.. image:: https://img.shields.io/github/license/ZubeidHendricks/azure-devops-mcp-server.svg
   :target: https://github.com/ZubeidHendricks/azure-devops-mcp-server/blob/main/LICENSE

Overview
--------

Azure DevOps MCP Server is a powerful Python library for interacting with Azure DevOps through the Model Context Protocol (MCP).

Features
--------

- Comprehensive project management
- Repository operations
- Work item tracking
- Team member insights
- Build definition monitoring

Installation
------------

.. code-block:: bash

   pip install azure-devops-mcp-server

Quick Start
-----------

.. code-block:: python

   from azure_devops_mcp import AzureDevOpsMCPServer

   # Initialize the server
   server = AzureDevOpsMCPServer('your-org', 'your-pat')

   # List projects
   projects = server.list_projects()

API Reference
-------------

.. toctree::
   :maxdepth: 2

   api/server

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
