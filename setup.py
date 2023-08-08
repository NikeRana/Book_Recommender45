from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Nike_Rana"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy','scikit-learn']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/NikeRana",
    author_email="cordate084@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.11",
    install_requires=LIST_OF_REQUIREMENTS
)
