# Automating CV and Resume creation from CSV
Author: Marlin Figgins

This is a weekend project I built to learn Snakemake and to practice generating .tex and .pdf documents using Python. The goal of this project is to enable users to build their own resume or academic CV with a template. 

## How to use

Edit config.yaml and postitions.yaml with personal details.

```bash
snakemake --cores 1 --use-conda
```

Create `my_config.yaml` which will take your name and contact information and upload a `my_positions.csv` which gives your education, work experience, ectera.
```python
snakemake
```
## Features 

Allows the user to build their own machine-readable resume using Python directly from a .csv.

Supported entry types:
- education
- experience
- research
- service
- honors
- service
- pub
- publicpub
- confpres

## Output

An example academic CV can be found in `output/academic_cv_John_H._Doe.pdf`.

## To do:
- [] Work on class files for resume and CV
- [] Add to pipeline, so that .tex and .pdf end up in the outputs folder.
- [] Go through and comment code
- Write tutorial and give guide on how to use this
- [] Add general class mapping, so that I can make whichever section go to whatever entry environment I please
- [] Make sure python knows to escape certain characters.
- [x] Create "John Doe" configuration for github upload
  - `sample_config.yaml` and `sample_input.csv` and `sample_cv` and `sample_resume`
