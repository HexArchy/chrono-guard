from setuptools import setup, find_packages

setup(
    name="ChronoGuard",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyQt6==6.4.0",
    ],
    entry_points={
        "console_scripts": [
            "chronoguard=main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A time-limited application with usage restrictions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HexArchy/chronoguard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
