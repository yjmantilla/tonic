import setuptools

setuptools.setup(
    name="tonic",
    description="Tonic RL Library",
    url="https://github.com/fabiopardo/tonic",
    version="0.3.0",
    author="Fabio Pardo",
    author_email="f.pardo@imperial.ac.uk",
    license="MIT",
    python_requires=">=3.6",
    keywords=["tonic", "deep learning", "reinforcement learning"],
    install_requires=[
        "gym", "matplotlib", "numpy", "pandas", "pyyaml", "termcolor"
    ],
    packages=[
        "tonic",
        "tonic.agents",
        "tonic.environments",
        "tonic.explorations",
        "tonic.replays",
        "tonic.tensorflow",
        "tonic.torch",
        "tonic.utils",  # 🔥 Explicitly list utils!
    ],
    include_package_data=True,
    zip_safe=False,  # Prevents import issues caused by zip compression
)
