from setuptools import setup, find_packages

setup(
    name="ezLineNotify",
    version="0.0.0.4",
    license="MIT",
    description="Use LINE Notify from Python.",
    
    author="Rilm2525",
    author_email="rilm2525ce@gmail.com",
    url="https://twitter.com/Rilm2525",
    
    install_requires=[
        "requests",
        "pillow",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
