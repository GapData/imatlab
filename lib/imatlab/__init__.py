import setuptools_scm
try:
    __version__ = setuptools_scm.get_version(  # xref setup.py
        root="../..", relative_to=__file__,
        version_scheme="post-release", local_scheme="node-and-date")
except LookupError:
    try:
        from ._version import version as __version__
    except ImportError:
        pass
