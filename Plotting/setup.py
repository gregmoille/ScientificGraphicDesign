from setuptools import setup

setup(
    name="pyprettyplot",
    version="1.0",
    packages=["pyprettyplot"],
    description="Pretty Plotter For Plotly",
    url="https://github.com/gregmoille/ScientificGraphicDesign/tree/main/Plotting/pyprettyplot",
    author="Greg Moille",
    author_email="gmoille@umd.edu",
    license="Open",
    install_requires=[
        "pandas",
        "scipy",
        "numpy",
        "matplotlib",
        "plotly",
        "cmcrameri",
        "SecretColors",
        "nbformat",
        "kaleido",
    ],
    include_package_data=True,
    zip_safe=False,
)
