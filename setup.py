from setuptools import setup, find_packages

setup(
    name='pyrrency_converter',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'python-dotenv',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'currency_converter=currency_converter:main',
        ],
    },
)