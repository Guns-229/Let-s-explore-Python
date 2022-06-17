import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mayadiff",
    version="0.0.2",  # check PEP: 440
    author="Mayank Johri",
    author_email="mayankjohri@gmail.com",
    description="An Application to create a diff between two folders/files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sourceforge.net/projects/pyfoldercompare",
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts=["mayadiff/cmpfiles.py", "mayadiff/img_cmp.py", "mayadiff/slate.py"],
    package_data={
        "docs": ["mayadiff/doc/*"],

        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU 3 License",
        "Operating System :: OS Independent",
    ],
)
