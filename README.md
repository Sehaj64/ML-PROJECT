# ML-PROJECT: Salary Prediction

This project implements a machine learning model to predict salaries based on various features. It includes data generation, model training, and a Flask web application for interaction.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
- [Running the Project](#running-the-project)
  - [1. Generate Data](#1-generate-data)
  - [2. Train the Model](#2-train-the-model)
  - [3. Run the Web Application](#3-run-the-web-application)
- [Exploring the Jupyter Notebook](#exploring-the-jupyter-notebook)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Data Generation:** Synthetic data for training and testing the model.
- **Machine Learning Model:** A Random Forest Regressor for salary prediction.
- **Web Application:** A Flask-based interface to interact with the trained model.
- **Jupyter Notebook:** Detailed exploratory data analysis, model development, and evaluation.

## Project Structure
```
ML-PROJECT/
├── app/
│   ├── static/               # Static files for the web app (CSS, JS, images)
│   ├── templates/            # HTML templates for the web app
│   └── app.py                # Flask web application main file
├── data/                     # Directory for generated data (created after running generate_data.py)
├── models/                   # Directory for trained models (created after running train.py)
├── venv/                     # Python virtual environment (created after setup)
├── .git/                     # Git repository files
├── .github/                  # GitHub specific configurations (e.g., CI/CD workflows)
├── .pytest_cache/            # Cache for pytest
├── .gitignore                # Specifies intentionally untracked files to ignore
├── conftest.py               # Pytest configuration file
├── generate_data.py          # Script to generate synthetic datasets
├── modify_notebook.py        # Script to modify the Jupyter notebook (internal use)
├── README.md                 # Project README file (this file)
├── requirements.txt          # List of Python dependencies
├── salary_prediction_analysis.ipynb # Jupyter Notebook for EDA and model analysis
└── train.py                  # Script to train the machine learning model
```

## Setup and Installation

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/Sehaj64/ML-PROJECT.git
cd ML-PROJECT
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install all the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Running the Project

Ensure your virtual environment is activated before running the following commands.

### 1. Generate Data

Generate the synthetic datasets required for the model:

```bash
python generate_data.py
```
This will create a `data` directory in the project root containing `ML case Study.csv`, `Colleges.csv`, and `cities.csv`.

### 2. Train the Model

Train the machine learning model. This script will preprocess the generated data and save the trained model.

```bash
python train.py
```
A `models` directory will be created, and the `random_forest_model.joblib` and `scaler.joblib` files will be saved inside it.

### 3. Run the Web Application

Start the Flask web application to interact with the trained model:

```bash
# Navigate into the 'app' directory
cd app

# Run the Flask application
python app.py
```
The application will typically be accessible at `http://127.0.0.1:5000` in your web browser.

## Exploring the Jupyter Notebook

To delve into the data analysis, feature engineering, and model evaluation steps, you can open the Jupyter Notebook:

```bash
# Ensure you are in the root ML-PROJECT directory
# If you are in the 'app' directory, navigate back: cd ..
jupyter lab
# or jupyter notebook
```
A new tab will open in your browser, from where you can navigate to `salary_prediction_analysis.ipynb` and execute its cells.

## Contributing
Feel free to fork the repository, open issues, and submit pull requests.

## License
[Specify your license here, e.g., MIT, Apache 2.0]