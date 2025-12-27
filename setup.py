"""
Setup file for the Todo CLI Application.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="todo-cli-app",
    version="1.0.0",
    author="Todo CLI Team",
    author_email="todo@example.com",
    description="A simple command-line interface application for managing todo tasks in memory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/todo-cli-app",
    packages=find_packages(where="src", include=["src.*"]),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.13",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "todo=cli.main:main",
        ],
    },
)