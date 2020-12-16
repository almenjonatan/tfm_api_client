import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tfm_client",
    version="0.0.2",
    author="Jonatan Almen",
    author_email="almen.jonatan@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/almenjonatan/tfm_api_client",
    packages=["tfm_client"],
    package_dir={"tfm_client": "tfm_client"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)