import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fruit_dash',
    version='1.0.0',
    python_requires='>=3.6.0',
    author='Sourav',                          
    author_email='souravnair314@gmail.com',      
    description='A fruit collecting terminal racing game', 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Souravnair07/fruit_dash_project',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'fruit_dash = fruit_dash.__main__:main'
        ]
    },
    install_requires=[
        'windows-curses >= 2.0;platform_system=="Windows"'
    ]
)
