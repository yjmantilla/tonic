import setuptools

setuptools.setup(
    name='tonic',
    description='Tonic RL Library',
    url='https://github.com/fabiopardo/tonic',
    version='0.3.0',
    author='Fabio Pardo',
    author_email='f.pardo@imperial.ac.uk',
    license='MIT',
    python_requires='>=3.6',
    keywords=['tonic', 'deep learning', 'reinforcement learning'],
    install_requires=[
        'gym', 'matplotlib', 'numpy', 'pandas', 'pyyaml', 'termcolor'
    ],
    packages=setuptools.find_packages(include=["tonic", "tonic.*"]),  # Ensures all submodules are included
    include_package_data=True,  # Ensures additional files are included
    zip_safe=False,  # Ensures files are not installed as a zip (avoids import issues)
)
