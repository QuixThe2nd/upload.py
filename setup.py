from setuptools import setup

with open('README.md', 'r') as fh:
   long_description = fh.read()
setup(
    name='upload.py',
    version='0.17',
    description='An mutiple upload service library',
    url='https://github.com/CrafterPika/upload.py',
    author='upload.py',
    author_email='crafterpika@email.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='The Unlicense',
    packages=['upload_py'],
    install_requires=['requests',
                      'BeautifulSoup4',
                      ],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.8',
    ],
)
