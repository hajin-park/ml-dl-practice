# Machine Learning / Deep Learning Practice

## Dive Into Deep Learning

###### 1st Edition - December 2023

## Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow

###### 3rd Edition - October 2022

## Machine Learning with Pytorch and Scikit-Learn

###### 1st Edition - February 2022

---

## Development

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
