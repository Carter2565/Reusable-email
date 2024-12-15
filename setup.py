from setuptools import setup, find_packages

setup(
    name="reusable.email",
    version="1.0.0",
    author="Carter2565, Jam",
    author_email="Carter@carter2565.dev",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "requests",
        "aiohttp",
        "typing_extensions"
    ],
    description="A reusable email handling package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)
