from setuptools import setup

setup(
    name='pyvrep',
    packages=['pyvrep', 'pyvrep.vrep'],
    version='0.2.1',
    description='Simple Python binding for V-REP robotics simulator',
    url='https://github.com/AAAI-DISIM-UnivAQ/vrep-api-python',
    author='giodegas',
    author_email='giovanni@giodegas.it',
    license='MIT',
    keywords='V-REP virtual robotics simulator binding api',
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    data_files=[('scenes', ['scenes/Pioneer.ttt', 'scenes/testAllComponents.ttt'])]
)
