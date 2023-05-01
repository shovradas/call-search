from setuptools import setup, find_namespace_packages

setup(
    name='iwu_callse',
    version='0.1.0',
    author='Shovra Das',
    author_email = "shovradas@gmail.com",
    description='IWU Project Call Search Engine',
    long_description=open('README.md').read(),
    python_requires='>=3.9, <4',
    package_dir={'': 'src'},
    packages=find_namespace_packages(
        include=['iwu.*'],
        where='src'
    ),
    install_requires=[
        'Flask==2.3.2',
        'feedparser==6.0.10',
        'requests==2.28.2',
        'beautifulsoup4==4.11.2'
    ],
    extras_require={
        'test': ['pytest==7.2.0'],
        'build': ['wheel==0.38.4']
    },
    entry_points={
        'console_scripts': [
            'iwu-callse=iwu.callse.app:main'
        ]
    }
)