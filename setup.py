from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='validCSV',
    version='0.0.1',    
    description='A small and performance-oriented CSV header linter / verifier',
    url='https://github.com/bmalbusca/validCSV',
    author='Bruno Figueiredo',
    author_email='bmalbusca@protonmail.com',
    license='MIT',
    packages=['validCSV'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8',
    ],
)
