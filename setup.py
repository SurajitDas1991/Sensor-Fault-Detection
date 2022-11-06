from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

## edit below variables as per your requirements -
REPO_NAME = "Sensor-Fault-Detection"
AUTHOR_USER_NAME = "SurajitDas1991"
SRC_REPO = "sensor"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Sensor Fault Detection Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="dsurajitd@gmail.com",
    packages=find_packages(),
    package_data={p: ["*"] for p in find_packages()},
    license="MIT",
    python_requires="==3.8",
    install_requires=required
)
