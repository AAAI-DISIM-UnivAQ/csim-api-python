from setuptools import setup

setup(
    name='pycsim',
    packages=['pycsim', 'pycsim.csim'],
    version='0.3.0',
    description='Simple Python binding for Coppelia SIM robotics simulator',
    url='https://github.com/AAAI-DISIM-UnivAQ/csim-api-python',
    author='giodegas',
    author_email='giovanni@giodegas.it',
    license='MIT',
    keywords='C-SIM virtual robotics simulator binding api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    data_files=[('scenes', ['scenes/Pioneer.ttt', 'scenes/testAllComponents.ttt'])]
)
