configfile: "config/config.yaml"
conda_environment = "envs/environment.yaml"

AutomateCV_config = "config/config.yaml"
name_ = config["contact_info"]["name"].replace(" ","_")
output_class = config["metadata"]["output_class"]
file_name = f"{output_class}_{name_}"

rule all:
  input:
    f"output/{file_name}.tex",
    f"output/{file_name}.pdf"

rule generate_tex:
  message: "Generating {output.tex_file} from {params.AutomateCV_config}."
  conda: conda_environment
  params:
    AutomateCV_config = AutomateCV_config
  output: 
    tex_file = f"src/{file_name}.tex"
  shell: "python3 scripts/automake_CV.py '{params.AutomateCV_config}'"
  
rule generate_pdf:
  message: "Generating {output.pdf_file} from {input.tex_file}"
  input:
    tex_file = rules.generate_tex.output.tex_file
  output: 
    pdf_file = f"src/{file_name}.pdf"
  shell: "latexmk -cd -e -f -pdf -interaction=nonstopmode -synctex=1 {input.tex_file}"

rule move_files:
  message: "Moving {params.file_name}* files to output folders"
  params: 
    file_name = file_name
  input:
    src_tex = rules.generate_tex.output.tex_file,
    src_pdf = rules.generate_pdf.output.pdf_file,
  output:
    f"output/{file_name}.tex",
    f"output/{file_name}.pdf"
  shell: "mv src/{params.file_name}* output/"
