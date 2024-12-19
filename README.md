# Data Science Self-Study Path

## Programming Fundamentals

### R for Data Science - 2nd Edition

### MATLAB Programming Fundamentals - R2023a

### Fluent Python - 2nd Edition

### T-SQL Fundamentals - 4th Edition

---

## Math Fundamentals

### An Introduction to Mathematical Statistics and Its Applications - 6th Edition

### OpenIntro Statistics - 4th Edition

### A First Course in Probability - 10th Edition

### Probability, Statistics, and Data: A Fresh Approach Using R - 1st Edition

---

## Modeling

### Applied Predictive Modeling - 1st Edition

### The Elements of Statistical Learning - 2nd Edition

### Introduction to Statistical Learning with R - 1st Edition

### Introduction to Statistical Learning with Python - 1st Edition

---

## Data Engineering

### Python for Data Analysis - 3rd Edition

### Python Data Science Handbook - 2nd Edition

### SQL for Data Scientists - 1st Edition

---

## Advanced Modeling (Frameworks, Deep Learning, Systems)

### Machine Learning with PyTorch and Scikit-learn - 1st Edition

### Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow - 3rd Edition

### Designing Machine Learning Systems - 1st Edition

### Dive Into Deep Learning

## Advanced Data Engineering (Platforms, Systems)

### Designing Data-Intensive Applications - 1st Edition

### [Apache Spark](https://spark.apache.org/)

[TODO] - i have not explored data engineering/warehousing/analysis very much yet

---

## Running code

1. Install
   [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
   or [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/).
2. Create the environment: _With GPU (Windows):_
    ```
    conda env create -f environment.yml
    ```
    _With CPU (Windows):_
    ```
    conda env create -f environment_cpu.yml
    ```
3. Make sure you can activate the environment:
    ```
    conda activate [pytorch/tensorflow]-practice-[gpu/cpu]
    ```
4. cd into the relevant directory
    ```
    cd [pytorch/tensorflow]-practice
    ```
5. And run the tests:
    ```
    python check_cuda.py
    python check_cpu.py
    ```
