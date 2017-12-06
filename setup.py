from setuptools import setup, find_packages


print(find_packages())

setup(
    name='megatroniki',
    version='1.0.0',
    description='simple python markdown wiki with web ui and commandline interface',
    author='Ethan Gallagher, Brian Konzman, Katie Schwegman',
    author_email='megatroniki2017@gmail.com',
    url='https://github.com/konzy/CSC440-Wiki-Project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=0.9',
        'Click>=6,<7',
        'Flask-Login>=0.4',
        'Flask-WTF>=0.8',
        'Markdown>=2.2.0',
        'Pygments>=1.5',
        'WTForms>=1.0.2',
        'Werkzeug>=0.8.3',
        'Pypandoc>=1.4'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock'],
    entry_points={
        'console_scripts': [
            'wiki=wiki.cli:main'
        ]
    },
    long_description="""\
    Megatroniki: A simple markdown based wiki
    -------------------------------------
    
    Create a wiki with user login, create, edit, delete, wiki pages.
    With features of google scholar lookup, download as pdf, email updated on page change.
    """
)
