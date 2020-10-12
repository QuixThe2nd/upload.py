from setuptools import setup

setup(
    name='upload.py',
    version='0.1.1',
    description='An mutiple upload service library',
    url='https://github.com/CrafterPika/upload.py',
    author='upload.py',
    author_email='crafterpika@email.com',
    license='The Unlicense',
    packages=['upload_py'],
    install_requires=['requests',
                      'BeautifulSoup4',
                      ],

    classifiers=[
        'Development Status :: Done',
        'Intended Audience :: Utility',
        'License :: The Unlicense',
        'Operating System :: Windows',
        'Programming Language :: Python :: 3.8',
    ],
)
