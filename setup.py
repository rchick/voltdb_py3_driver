import setuptools

version = "0.0.1"

install_requires = (
    "gssapi",
)

setuptools.setup(
    name="VoltDB Py3 driver",
    version=version,
    author="Alex Kotenko",
    author_email="alex.kotenko@blockex.com",
    packages=(
        "VoltDB python3 driver",
    ),
    install_requires=install_requires,
)
