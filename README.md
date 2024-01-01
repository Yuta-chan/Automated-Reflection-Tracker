# Automated Reflection Tracker

This repository contains a Python script that automates the process of recording and reflecting on various topics. When executed, it initiates an interactive session that prompts the user to evaluate and reflect upon a specific subject. The responses, along with a timestamp, are then saved in a CSV file within a `files` directory.

## Features

- **Interactive Prompting**: The script asks a series of questions to guide the user through their reflection process.
- **Automatic CSV Creation**: User responses are collected and saved in a versioned CSV file for easy tracking and future reference.
- **Reflection Archive**: Maintains an archive of reflections by automatically incrementing the file version.
- **Data Visualization**: Utilizes Pandas for data handling and Matplotlib for potential future visualizations of the recorded reflections.

## Getting Started

To use this script, simply clone the repository and execute the script in your preferred Python environment.

```bash
git clone https://github.com/yourusername/automated-reflection-tracker.git
cd automated-reflection-tracker
python reflection_tracker.py
```

Follow the on-screen prompts to input your reflections.

## CSV File Structure
The generated CSV files will have the following columns:

- **Field**: The topic or subject of reflection.
- **Feeling**: A personal rating of feelings towards the subject on a scale of 0 to 10.
- **Impact**: The assessed impact of the subject on the user's life on a scale of 0 to 10.
- **Note**: Additional remarks or notes about the subject.
- **Date**: The date on which the reflection was recorded.

## Data Visualization
The script includes a preliminary setup for data visualization using Pandas and Matplotlib. This feature will be expanded in future updates to provide insightful charts and tables based on the accumulated reflection data.

## Requirements
+ Python 3.x
+ Pandas
+ Matplotlib

Ensure you have the required libraries installed by running:

```bash
pip install pandas matplotlib
```
