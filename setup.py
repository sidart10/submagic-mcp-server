#!/usr/bin/env python3
"""
Setup configuration for Submagic MCP Server
Enables installation via pip for easy distribution
"""

from setuptools import setup, find_packages

# Read the README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="submagic-mcp-server",
    version="1.0.0",
    author="Sid Dani",
    author_email="",  # Add your email if desired
    description="AI-powered video editing MCP server with Submagic API integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidart10/submagic-mcp-server",
    project_urls={
        "Bug Tracker": "https://github.com/sidart10/submagic-mcp-server/issues",
        "Documentation": "https://github.com/sidart10/submagic-mcp-server#readme",
        "Source Code": "https://github.com/sidart10/submagic-mcp-server",
    },
    py_modules=["submagic_mcp"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "submagic-mcp=submagic_mcp:main",
        ],
    },
    keywords="mcp modelcontextprotocol video-editing ai submagic captions automation",
    # MCP Registry validation metadata
    mcpName="io.github.sidart10/submagic-mcp-server",
)

