import pandas as pd
import shutil
import yaml
import sys
from automake_CV_helpers import parse_dates


class automate_CV:
    def __init__(self, config="config/config.yaml"):

        self.get_config_yaml(config)

        self.name = self.config["contact_info"]["name"]
        self.email = self.config["contact_info"]["email"]
        self.url = self.config["contact_info"]["website"]
        self.phone = self.config["contact_info"]["phone"]
        self.output_class = self.config["metadata"]["output_class"]

        # get data_frame
        self.get_df()
        self.process_df()

        # Creating base file name used throughout
        name_ = self.name.replace(" ", "_")
        self.file_name = f"{self.output_class}_{name_}"

    def get_config_yaml(self, config):
        with open(config) as yaml_file:
            self.config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    def get_df(self):
        self.df = pd.read_csv(self.config["metadata"]["input_data"])

    def process_df(self):
        self.df["dates"] = self.df.apply(
            lambda x: parse_dates(x["start_date"], x["end_date"]), axis=1
        )
        self.df.drop(columns=["start_date", "end_date"], inplace=True)

        if self.output_class == "academic_cv":
            self.df.drop(columns=["description_short"], inplace=True)
        if self.output_class == "resume":
            self.df.drop(columns=["description_long"], inplace=True)

        # Description variable should always be last
        cols = self.df.columns.tolist()
        cols[-1], cols[-2] = cols[-2], cols[-1]

        self.df = self.df[cols]

    def create_new_file(self):
        shutil.copyfile(
            f"src/{self.output_class}_template.tex",
            f"src/{self.file_name}.tex"
        )

    # Adding data to .tex file
    def add_contact_info(self):
        # Read in your .tex file
        tex_file_dir = f"src/{self.file_name}.tex"
        tex_file = open(tex_file_dir, "rt")
        text = tex_file.read()

        # Replace Placeholder Values
        text = text.replace("$name", self.name)
        text = text.replace("$email", self.email)
        text = text.replace("$url", self.url)
        text = text.replace("$phone", self.phone)

        tex_file.close()  # close .tex file

        # Open and overwrite file with your contact info
        tex_file = open(tex_file_dir, "wt")
        tex_file.write(text)
        tex_file.close()

    def add_section(self, section_name):
        self.add_before_doc_end(text=f"\section{{{section_name}}} \n")

    def add_entry(self, row):
        commandname = "\\" + row[0] + "entry"

        if not self.needs_description:
            row = row[0:-1]
        # For each non-nan entry, put between brackets {} to form entry command
        row_info = [f"{{{value}}}" for index, value in row.dropna().items()]
        text = f"{commandname}" + "".join(row_info[1:])

        if self.needs_enumeration:
            self.add_before_doc_end(
                text=f"\item {text} \n"
            )  # Things in list need \item
        else:
            self.add_before_doc_end(text=f"{text} \n")

    def add_before_doc_end(self, text):
        # Open document insert text at second to last line
        with open(f"src/{self.file_name}.tex", "rt") as file:
            lines = file.readlines()
            lines.insert(-2, f"{text}")

        with open(f"src/{self.file_name}.tex", "wt") as file:
            file.write("".join(lines))

    def get_section_titles(self):
        return self.config["section_titles"]

    def get_section_order(self):
        return self.config["section_order"]

    def section_description(self, section):
        self.needs_description = section in self.config["needs_description"]

    def section_enumeration(self, section):
        self.needs_enumeration = section in self.config["needs_enumeration"]
        if self.needs_enumeration:
            self.add_before_doc_end("\ begin{enumerate} \n".replace(" ", ""))

    def begin_section(self, section):
        self.section_enumeration(section)
        self.section_description(section)

    def end_section(self, section):
        if self.needs_enumeration:
            self.add_before_doc_end("\end{enumerate} \n")

    def automate(self):
        self.create_new_file()  # Create new file
        self.add_contact_info()  # Retrieve contact information

        # Retrieve user-configured section-ordering and titling
        sections_ordered = self.get_section_order()
        section_titles = self.get_section_titles()

        for section in sections_ordered:  # Using custom sections
            self.add_section(section_titles[section])  # Add section title
            self.begin_section(section)  # Begin section
            for i, row in self.df.query(f"entry_type == '{section}'").iterrows():
                self.add_entry(row)
            self.end_section(section)  # End section

            self.add_before_doc_end("\n \n")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        MyCV = automate_CV(config=sys.argv[1])
        MyCV.automate()
    else:
        MyCV = automate_CV()
        MyCV.automate()
