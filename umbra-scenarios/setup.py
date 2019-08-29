from setuptools import setup, find_packages

setup(name='umbra-scenarios',
      version='0.1',
      description='Hyperledger Labs: Project Umbra - Scenarios System',
      author='Raphael Vicente Rosa',
      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      keywords=('Hyperledger', 'Labs', 'Umbra'),
      license='Apache License v2.0',
      url='https://github.com/raphaelvrosa/umbra',
      download_url='https://github.com/raphaelvrosa/umbra',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.0',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
      ],
      install_requires = [
        'gevent',
        'requests',
        'Flask',
        'Flask-RESTful',
        'psutil',
        'PyYAML',
      ],
)