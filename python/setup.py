from setuptools import find_packages, setup
from setuptools_rust import Binding, RustExtension

setup(
    name="jsonschema_rs",
    version="0.3.0",
    description="Fast JSON Schema validation for Python implemented in Rust",
    long_description=open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",
    keywords="jsonschema validation rust",
    author="Dmitry Dygalo",
    author_email="dadygalo@gmail.com",
    maintainer="Dmitry Dygalo",
    maintainer_email="dadygalo@gmail.com",
    python_requires=">=3.5",
    url="https://github.com/Stranger6667/jsonschema-rs/python",
    license="MIT",
    rust_extensions=[RustExtension("jsonschema_rs.jsonschema_rs", binding=Binding.PyO3)],
    extras={"tests": ["pytest", "hypothesis"], "bench": ["pytest-benchmark"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Rust",
    ],
    packages=find_packages(where="pysrc"),
    package_dir={"": "pysrc"},
    zip_safe=False,
)
