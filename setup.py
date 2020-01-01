from setuptools import setup

setup(
    name="my_cookies",
    packages=["my_cookies"],
    version="0.1",
    license="MIT",
    description="Retrieve chrome cookies",
    author="Wang Kai",
    author_email="kaiwkx@gmail.com",
    url="https://github.com/kaiwk/my_cookies",
    download_url="https://github.com/kaiwk/my_cookies",
    keywords=["chrome", "cookies"],
    scripts=['bin/my_cookies'],
    install_requires=["pycryptodome", "keyring"],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta", or "5 - Production/Stable"
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
