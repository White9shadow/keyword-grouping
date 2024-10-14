
# keyword-grouping

## Keyword Processing Scripts: A Quick Guide

This repository provides a straightforward approach to processing keyword data using Python scripts. The scripts are designed to handle keyword data in both text (TXT) and CSV formats.

### Script Owner
This project is maintained by **revWhiteShadow**.

## Table of Contents

1. [Cloning the Repository](#cloning-the-repository)
2. [Installation](#installation)
3. [Preparing Your Keyword Files](#preparing-your-keyword-files)
4. [Running the Scripts](#running-the-scripts)

## Cloning the Repository

To get started, follow these steps to clone the repository:

1. Open your terminal.

2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/White9shadow/keyword-grouping.git
   ```

3. Navigate into the cloned directory:

   ```bash
   cd keyword-grouping
   ```

## Installation

After navigating into the project directory, install the required libraries:

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the required libraries using pip by running the following command:

   ```bash
   pip install pandas scikit-learn nltk
   ```

## Preparing Your Keyword Files

Follow these steps to prepare your keyword files:

1. **For Text Files (TXT)**:
   - Create a file named `input.txt` and copy your keywords into this file.

2. **For CSV Files**:
   - If you've downloaded CSV files from SEMrush or other platforms, rename the file to `input.csv`.

## Running the Scripts

After preparing your keyword files, you can run the respective scripts based on the format of your input file:

1. **For CSV Files**:
   - Open your terminal and run the following command:

     ```bash
     python kg-csv.py
     ```

   - This command processes the keywords in `input.csv` and outputs the sorted keywords to `csv_sorted_keywords_output.csv`.

2. **For Text Files**:
   - Open your terminal and run the following command:

     ```bash
     python kg-txt.py
     ```

   - This command processes the keywords in `input.txt` and outputs the sorted keywords to `txt_sorted_keywords_output.txt`.

