import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="testcase-automaker",
    version="1.0.8",
    author="Yuyi Shao",
    author_email="523314409@qq.com",
    description="testcase-automake base on pairwise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amazingTest/testcase-automaker",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ),
)