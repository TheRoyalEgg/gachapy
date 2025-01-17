import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gachapy",
    version="0.1.5",
    author="Jacob Kerr",
    author_email="jck268@cornell.edu",
    description="A gacha engine built in Python for developing gacha games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakejack13/gachapy",
    project_urls={
        "Bug Tracker": "https://github.com/jakejack13/gachapy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)