from setuptools import setup, find_packages

setup(
    name="AI_Career_Recommendation",  # Name of the package
    version="0.1",  # Initial version of your package
    packages=find_packages(),  # Automatically finds all packages in the directory
    install_requires=[  # List of dependencies that your package requires
        'pandas',        # For data handling
        'streamlit',     # For the interactive web app
        'networkx',      # For graph creation
        'matplotlib',    # For plotting graphs
    ],
    entry_points={  # Optional entry point for running your app as a command line tool
        'console_scripts': [
            'career-recommendation=src.streamlit_app:main',  # Assuming you have a 'main' function in streamlit_app.py
        ],
    },
    author="Ovi Miraz",  # Replace with your name
    author_email="sarker15-4736@diu.edu.bd",  # Your email address
    description="A career recommendation system based on A* search algorithm",  # Brief description of your project
    long_description=open('README.md').read(),  # Full description from README.md
    long_description_content_type='text/markdown',  # Format of the long description
    url="https://github.com/ovimiraz33/AI_Career_Recommendation",  # URL of the GitHub repository
    classifiers=[  # Additional information about the package for PyPI
        "Programming Language :: Python :: 3",  # Python version
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # Platform compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version
)
