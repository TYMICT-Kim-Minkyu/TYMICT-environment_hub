from setuptools import setup, find_packages

setup(
    name='pycaret_for_me',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'pycaret[full]',
        'xgboost',
        'lightgbm',
        'catboost',
        'imbalanced-learn',
        'mlxtend',
        'sqlalchemy',
        'pyod',
    ],
    python_requires='>=3.11',  # Python 3.11 이상을 요구
)
