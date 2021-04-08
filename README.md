# Automating CV and Resume creation from CSV
Author: Marlin Figgins

This is a weekend project I built to learn Snakemake and to practice generating .tex and .pdf documents using Python. The goal of this project is to enable users to build their own resume or academic CV with a template. 

## How to use

Create conda environment and download dependencies

```bash
conda env create --name automateCV --file envs/environment.yaml
```

Load conda environment 
```bash
conda activate automateCV 
```

Create `my_config.yaml` which will take your name and contact information and upload a `my_positions.csv` which gives your education, work experience, ectera.
```python
snakemake
```
## Features 

Allows the user to build their own machine-readable resume using Python directly from a .csv.


## To do:
- [] Work on class files for resume and CV
- [] Add to pipeline, so that .tex and .pdf end up in the outputs folder.
- [] Go through and comment code
- Write tutorial and give guide on how to use this
- [] Add general class mapping, so that I can make whichever section go to whatever entry environment I please
- [] Create "John Doe" configuration for github upload
  - `sample_config.yaml` and `sample_input.csv` and `sample_cv` and `sample_resume`
