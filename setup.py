from setuptools import setup, find_packages
setup(
    name='blackiceprog',
    packages=find_packages(),
    install_requires=['pyserial'],
    version='1.0.0',
    description='Programmer for the blackice FPGAs by myStorm (https://mystorm.uk/)',
    author='Jaime Penalba Estebanez',
    author_email='jpenalbae@gmail.com',
    url='https://github.com/jpenalbae/black-iceprog',
    keywords=['fpga', 'blackice', 'programmer', 'bitstream', 'mystorm'],
    license='GNU General Public License v3.0',
    classifiers=[],
    entry_points={
        'console_scripts':[
            'black-iceprog = blackiceprog.__main__:main'
        ]
    },
)
