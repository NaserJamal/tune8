from setuptools import setup, find_packages

setup(
    name='tune8',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'tune8=tune8.app:run_app',
        ],
    },
)