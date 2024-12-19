a semi-structured guide to pursuing data science after hours of googling

## Programming Fundamentals

- ### R for Data Science - 2nd Edition

- ### MATLAB Programming Fundamentals - R2023a

- ### Fluent Python - 2nd Edition

- ### T-SQL Fundamentals - 4th Edition

---

## Math Fundamentals

- ### An Introduction to Mathematical Statistics and Its Applications - 6th Edition

- ### OpenIntro Statistics - 4th Edition

- ### A First Course in Probability - 10th Edition

- ### Probability, Statistics, and Data: A Fresh Approach Using R - 1st Edition

---

## Modeling

1. ### Applied Predictive Modeling - 1st Edition

2. ### The Elements of Statistical Learning - 2nd Edition

- ### An Introduction to Statistical Learning with R - 2nd Edition

-  ### An Introduction to Statistical Learning with Python - 2nd Edition

---

## Data Engineering

1. ### Python for Data Analysis - 3rd Edition

2. ### Python Data Science Handbook - 2nd Edition

- ### SQL for Data Scientists - 1st Edition

---

## Advanced Modeling (Frameworks, Deep Learning, Systems)

- ### Machine Learning with PyTorch and Scikit-Learn - 1st Edition

- ### Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow - 3rd Edition

- ### Designing Machine Learning Systems - 1st Edition

- ### Dive Into Deep Learning

## Advanced Data Engineering (Platforms, Systems)

- ### Designing Data-Intensive Applications - 1st Edition

- ### [Apache Spark](https://spark.apache.org/)

[TODO] - i have not explored data engineering/warehousing/analysis very much yet

---

## Public Datasets

 - [The Open Science Framework](https://osf.io/)
 - [DATA.NASA.GOV](https://data.nasa.gov/)
 - [U.S. Government's Open Data](https://data.gov/)
 - [Office for National Statistics](https://www.ons.gov.uk/)
 - [Papers With Code](https://paperswithcode.com/datasets)
 - [Hugging Face](https://huggingface.co/datasets)
 - [Kaggle](https://www.kaggle.com/datasets)
 - [GitHub awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)
 - [Databar](https://databar.ai/)
 - [Reddit r/statistics](https://www.reddit.com/r/statistics/)
 - [Google Dataset Search](https://datasetsearch.research.google.com/)
 - google, web scraping, your brain

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
