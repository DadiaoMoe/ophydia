# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='ofdc',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='0.1.0-beta.1',
    description='Ophydia Programming Language for Bytom',
    long_description_markdown_filename='README.md',
    author='DadiaoMoe',
    author_email='',
    url='https://github.com/DadiaoMoe/ophydia',
    license="MIT",
    keywords='bytom',
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.6',
    py_modules=['ofdc'],
    # install_requires=[
    #     'pycryptodome>=3.5.1,<4',
    # ],
    # setup_requires=[
    #     'pytest-runner'
    # ],
    # tests_require=[
    #     'pytest',
    #     'pytest-cov',
    #     'py-evm==0.2.0a32',
    #     'eth-tester[py-evm]==0.1.0b32',
    #     'web3==4.4.1',
    # ],
    scripts=[
        'bin/ofdc',
        # 'bin/vyper-serve',
        # 'bin/vyper-lll'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ]
)
