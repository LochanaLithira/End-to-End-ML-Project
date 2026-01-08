import setuptools

# Define the version of the package
__version__ = "0.0.1"

REPO_NAME = "end-to-end-ml-project"
AUTHOR_USER_NAME = "LochanaLithira"

# Setup function to define the package
setuptools.setup(
    name=REPO_NAME,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Author of the package
    description="A small python package for end to end ml project",  # Short description
    package_dir={"": "src"},  # Source directory
    packages=setuptools.find_packages(where="src"),  # Find packages in the source directory
)


