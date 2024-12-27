from setuptools import setup, find_packages

setup(
    name='azure-devops-mcp-server',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'azure-devops-python-api>=6.0.0',
        'requests>=2.28.0',
        'pydantic>=2.0.0',
    ],
    author='Zubeid Hendricks',
    author_email='zubeid.hendricks@gmail.com',
    description='MCP Server for Azure DevOps Integration by Zubeid Hendricks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ZubeidHendricks/azure-devops-mcp-server',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='azure-devops mcp server integration zubeid-hendricks'
)
