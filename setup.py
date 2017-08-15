import setuptools

version = "0.1.2"

install_requires = (
    "gssapi>=1.2.0",
    "pyjks>=17.1.0",
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
