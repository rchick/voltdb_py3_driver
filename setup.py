import setuptools

version = "0.0.1"

install_requires = (
    "gssapi",
)

setuptools.setup(
    name="voltdb_py3_driver",
    version=version,
    author="Alex Kotenko",
    author_email="alex.kotenko@blockex.com",
    packages=(
        "voltdb_py3_driver",
    ),
    install_requires=install_requires,
)
