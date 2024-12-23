a semi-structured guide to pursuing data science formed after hours of googling

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
   
---

## 1. Programming Fundamentals

-   ### R for Data Science - 2nd Edition

-   ### MATLAB Programming Fundamentals - R2023a

-   ### Fluent Python - 2nd Edition

-   ### T-SQL Fundamentals - 4th Edition

## 2. Math Fundamentals

-   ### A First Course in Probability - 10th Edition

-   ### Introduction to Probability - 1st Edition

-   ### An Introduction to Mathematical Statistics and Its Applications - 6th Edition

-   ### Mathematical Statistics with Applications - 7th Edition

-   ### OpenIntro Statistics - 4th Edition

-   ### Probability, Statistics, and Data: A Fresh Approach Using R - 1st Edition

-   Differential Calculus, Linear Algebra, ODEs/PDEs

## 3. Modeling

- ### Applied Predictive Modeling - 1st Edition

- ### The Elements of Statistical Learning - 2nd Edition

- ### An Introduction to Statistical Learning with R - 2nd Edition

- ### An Introduction to Statistical Learning with Python - 2nd Edition

## 4. Data Engineering

- ### Python for Data Analysis - 3rd Edition

- ### Python Data Science Handbook - 2nd Edition

- ### SQL for Data Scientists - 1st Edition

## 5. Advanced Modeling (Frameworks, Deep Learning, Systems)

-   ### Machine Learning with PyTorch and Scikit-Learn - 1st Edition

-   ### Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow - 3rd Edition

-   ### Designing Machine Learning Systems - 1st Edition

-   ### Dive Into Deep Learning - 1st Edition

-   ### Artificial Intelligence: A Modern Approach - 4th Edition

## 6. Advanced Data Engineering (Platforms, Systems)

-   ### Designing Data-Intensive Applications - 1st Edition

-   ### [Apache Spark](https://spark.apache.org/)

-   ### [Apache Hadoop](https://hadoop.apache.org/)

-   ### [Apache Flink](https://flink.apache.org/)

-   Cloud tool (AWS, GCP, Azure, etc...)

-   [TODO] data engineering/warehousing

## 7. Advanced Math

- ### Statistical Rethinking - 2nd Edition

- ### Statistical Inference - 2nd Edition

- ### Probability: Theory and Examples - 5th Edition

- ### An Introduction to Stochastic Modeling - 4th Edition

- ### Bayesian Data Analysis - 3rd Edition

---

## Interview Practice

-   [DataLemur](https://datalemur.com/)
-   [stratascratch](https://www.stratascratch.com/)
-   [Deep-ML](https://www.deep-ml.com/)
-   [NeetCode](https://neetcode.io/)
-   [Kaggle](https://www.kaggle.com/competitions)
-   [TidyTuesday](https://github.com/rfordatascience/tidytuesday)

## Online Courses/Certificates

- [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science)
- [Machine Learning Specialization - Andrew Ng](https://www.coursera.org/specializations/machine-learning-introduction)
- [Deep Learning Specialization - Andrew Ng](https://www.coursera.org/specializations/deep-learning)

## Public Datasets

-   [Registry of Open Data on AWS](https://registry.opendata.aws/)
-   [OpenML](https://www.openml.org/search?type=data&sort=runs&status=active)
-   [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/)
-   [The Open Science Framework](https://osf.io/)
-   [DATA.NASA.GOV](https://data.nasa.gov/)
-   [U.S. Government's Open Data](https://data.gov/)
-   [Office for National Statistics](https://www.ons.gov.uk/)
-   [Papers With Code](https://paperswithcode.com/datasets)
-   [Hugging Face](https://huggingface.co/datasets)
-   [Kaggle](https://www.kaggle.com/datasets)
-   [GitHub awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)
-   [Databar](https://databar.ai/)
-   [Reddit r/statistics](https://www.reddit.com/r/statistics/)
-   [Google Dataset Search](https://datasetsearch.research.google.com/)

---

Course Texts:

-   K. Korb and A. Nicholson, Bayesian Artificial Intelligence. (UCSD CSE 150a)
-   S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach. (UCSD
    CSE 150a) (UCSD CSE 150b) (UCM CSE176)
-   R. Sutton and A. Barto, Reinforcement Learning: An Introduction. (UCSD CSE
    150a)
-   The Elements of Statistical Learning by Trevor Hastie, ‎Robert Tibshirani,
    and Jerome Friedman. (UCSD CSE 151a)
-   Data Mining: Concepts and Techniques by Jiawei Han et al. (UCSD CSE 151a)
-   Pattern Recognition and Machine Learning by Christopher M. Bishop. (UCSD CSE
    151a)
-   Dive into Deep Learning book by Aston Zhang et al. (UCSD CSE 151a)
-   [Deep Learning](https://www.deeplearningbook.org/) (UCSD CSE 151b)
-   [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
    (UCSD CSE 151b)
-   [Learning From Data](https://work.caltech.edu/telecourse) (UCSD CSE 151b)
-   G. James, D. Witten, T. Hastie and R. Tibshirani: An Introduction to
    Statistical Learning, with Applications in R, 2nd ed. Springer, 2021 (UCM
    CSE176)
-   R. O. Duda, P. E. Hart and D. G. Stork: Pattern Classification, 2nd ed.
    Wiley, 2001. (UCM CSE176)
-   P. A. Flach: Machine Learning. The Art and Science of Algorithms That Make
    Sense of Data. Cambridge University Press, 2012 (UCM CSE176)
-   S. Marsland: Machine Learning: An Algorithmic Perspective, 2nd ed. Chapman
    and Hall/CRC Press, 2014 (UCM CSE176)
-   T. M. Mitchell: Machine Learning. McGraw-Hill, 1997 (UCM CSE176)
