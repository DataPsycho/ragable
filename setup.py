import logging
import os

from setuptools import find_packages, setup

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

NAMESPACE = "ragable"


def read_requirements() -> list:
    """Read requirements file"""
    with open("requirements/lib.txt") as fp:
        install_requires = fp.readlines()
        install_requires = [item.strip() for item in install_requires]
        pkgs = ", ".join(install_requires)
        logging.info(f"Following packages will be added as dependency: {pkgs}")
        return install_requires


def read_metadata() -> str:
    """Read the readme file for setup."""
    readme_txt = ""
    try:
        with open("README.md", "rt", encoding="utf-8") as f:
            readme_text = f.read()
            logging.info("Read me read successfully !")
            return readme_text
    except FileNotFoundError as e:
        print(e)
        return readme_txt
    except Exception as e:
        print(e)
        return readme_txt


def get_version_from_package():
    """Read the current version from the package"""
    with open(
        os.path.join("src", NAMESPACE, "__init__.py"), "rt", encoding="utf-8"
    ) as f:
        for line in f:
            if "VERSION" in line:
                version: str = line.split("=")[1]
                version = version.strip().replace('"', "")
                logging.info(f"The version tag will be used for the build: {version}")
                return version
    raise KeyError("Could not find the VERSION tag in the __init__.py file")


setup(
    name=NAMESPACE,
    version=get_version_from_package(),
    author="unknown",
    author_email="unknown.com",
    url="unknown.com",
    description="Authentifield model API provider",
    long_description=read_metadata(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    # package_dir={
    #     NAMESPACE: f"src/{NAMESPACE}",
    #     "auto_AD": f"src/{NAMESPACE}/model_template/src/auto_AD",
    #     "model_template": f"src/{NAMESPACE}/model_template/src"
    # },
    install_requires=read_requirements(),
    license="unknown",
    # license_files=("LICENSE",),
    keywords="AI Development",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 4 - Beta",
        "Environment :: Linux, MacOS X",
    ],
    zip_safe=False,
    include_package_data=True,
)


if __name__ == "__main__":
    read_requirements()
    read_metadata()
    get_version_from_package()