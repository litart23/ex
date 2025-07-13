from setuptools import setup, find_packages

setup(
    name="textgpt",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0"
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
)
