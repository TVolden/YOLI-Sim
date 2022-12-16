from setuptools import setup, find_packages

setup(
    name="gym_yoli",
    version="0.0.1",
    install_requires=["gym==0.21.0", "pygame==2.1.0"],
    packages=find_packages(where="gym_yoli"),
    package_dir={"": "gym_yoli"}
)
