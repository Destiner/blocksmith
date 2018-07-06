from setuptools import setup
setup(
    name = 'blocksmith',
    packages = ['blocksmith'],
    install_requires = ['ecdsa'],
    version = '1.1.3',
    description = 'Bitcoin key manipulation',
    author = 'Timur Badretdinov',
    author_email = 'destinerx@gmail.com',
    url = 'https://github.com/Destiner/blocksmith',
    keywords = ['security', 'cryptography', 'cryptocurrency', 'bitcoin'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries',
    ],
)
