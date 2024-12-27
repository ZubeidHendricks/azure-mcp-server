# Contributing to Azure DevOps MCP Server

## Welcome Contributors!

First off, thank you for considering contributing to the Azure DevOps MCP Server. It's people like you that make this project such a great tool for the community.

### About the Project

The Azure DevOps MCP Server is an open-source project designed to provide seamless integration with Azure DevOps through the Model Context Protocol (MCP). Our goal is to create a flexible, powerful, and easy-to-use tool for developers and teams.

## How to Contribute

There are many ways you can contribute to this project:

### 1. Reporting Bugs
- Use GitHub Issues to report bugs
- Provide a clear and detailed description
- Include steps to reproduce the issue
- Specify your environment (Python version, OS, etc.)

#### Bug Report Template
```markdown
**Describe the bug:**
A clear description of what the bug is.

**To Reproduce:**
Steps to reproduce the behavior:
1. Call method '...'
2. With parameters '...'
3. See error

**Expected behavior:**
What you expected to happen.

**Screenshots or Error Traceback:**
If applicable, add screenshots or error output.

**Environment:**
 - OS: [e.g., Windows 10, macOS 11]
 - Python Version: [e.g., 3.9.5]
 - Azure DevOps MCP Server Version: [e.g., 0.1.0]
```

### 2. Suggesting Enhancements
- Open a GitHub Issue
- Clearly describe the enhancement
- Explain the value it would bring
- Provide examples if possible

### 3. Contributing Code

#### Setup for Development
1. Fork the repository
2. Clone your fork
```bash
git clone https://github.com/your-username/azure-devops-mcp-server.git
cd azure-devops-mcp-server
```

3. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

4. Install development dependencies
```bash
pip install -r requirements.txt
pip install -e .[dev]
```

#### Coding Guidelines
- Follow PEP 8 style guidelines
- Write clear, commented code
- Add type hints
- Ensure comprehensive test coverage

#### Pull Request Process
1. Create a branch for your feature
```bash
git checkout -b feature/awesome-new-feature
```

2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
```bash
pytest tests/
```

5. Update documentation if needed
6. Commit with a clear message
```bash
git commit -m "Add feature: description of changes"
```

7. Push to your fork
```bash
git push origin feature/awesome-new-feature
```

8. Open a Pull Request against the main repository

#### Pull Request Template
```markdown
## Description
[Provide a detailed description of your changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested?
[Describe the tests you've added/run to verify changes]

## Checklist:
- [ ] My code follows the project's style guidelines
- [ ] I've added tests proving my fix/feature works
- [ ] Existing tests pass
- [ ] I've updated documentation
```

### 4. Development Environment

#### Required Tools
- Python 3.8+
- pip
- Git
- Azure DevOps account (for testing)

#### Recommended Tools
- VSCode or PyCharm
- Black (code formatter)
- Mypy (type checking)
- Pytest (testing)

### 5. Code of Conduct

#### Our Pledge
We are committed to providing a friendly, safe, and welcoming environment for all contributors.

#### Expected Behavior
- Be respectful and inclusive
- Be patient and helpful
- Assume good intentions
- Provide constructive feedback

### 6. Questions?

If you have questions or need help:
- Open a GitHub Issue
- Ask in discussion forums
- Reach out to the maintainers

## Thank You!

Your contributions make open-source software great. We appreciate your help in making the Azure DevOps MCP Server better for everyone.

Maintained by Zubeid Hendricks
