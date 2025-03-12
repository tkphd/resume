 # -*- coding: utf-8 -*-

from yaml import load as yaml_load
from yaml import Loader as yaml_loader

lilskip = "\\\\\n"
midskip = "\\\\[0.25\\baselineskip]\n"
bigskip = "\n\n"

with open("TKellerPhD.tex", "w") as resume:
    with open("header.tex") as header:
        for line in header.readlines():
            resume.write(line)

    resume.write("\\begin{resume}")

    with open("../_data/objective.yml") as obj_yml:
        resume.write("\\section{Objective}\n")
        obj_data = yaml_load(obj_yml, Loader=yaml_loader)
        resume.write(obj_data["objective"].replace("R&D", "R\&D"))
        resume.write("\\section{Qualified by}\n")
        resume.write("\\begin{itemize}\n")
        for qual in obj_data["qualifications"]:
            resume.write("\\item " + qual)
        resume.write("\\end{itemize}\n")

    with open("../_data/experience.yml") as exp_yaml:
        resume.write("\\section{Experience}\n")
        exp_data = yaml_load(exp_yaml, Loader=yaml_loader)
        for company in exp_data:
            if len(company["name"]) > 20:
                resume.write("{\\bf \href{" + company["home"] + "}{" + company["name"] + "}}" + midskip)
                resume.write("\\rightline{\href{" + company["url"] + "}{" + company["department"]
                             + ", " + company["location"] + "}}" + lilskip)
            else:
                resume.write("{\\bf \href{" + company["home"] + "}{" + company["name"] + "}}")
                resume.write("\hfill \href{" + company["url"] + "}{" + company["department"]
                             + ", " + company["location"] + "}" + lilskip)
            for position in company["positions"]:
                resume.write("\\textit{" + position["title"] + "} \hfill " + position["start"]
                             + " to " + position["until"] + lilskip)
                if "summary" in position:
                    resume.write(str(position["summary"]).replace("&times;", "$\\times$") + bigskip)

    with open("../_data/education.yml") as edu_yaml:
        resume.write("\\section{Education}\n")
        edu_data = yaml_load(edu_yaml, Loader=yaml_loader)
        for school in edu_data:
            resume.write("{\\bf \href{" + school["url"] + "}{" + school["name"] + "}} \\hfill "
                         + school["location"] + midskip)
            for degree in school["degrees"]:
                resume.write("\\textit{" + degree["name"] + "} in " + degree["field"] + "\\hfill "
                             + str(degree["start"]) + " to " + str(degree["until"]) + lilskip)
                if "thesis" in degree:
                    resume.write("Thesis: \\gapuline{" + degree["thesis"] + "}")
                if "summary" in degree:
                    resume.write(midskip)
                    resume.write(str(degree["summary"]).replace("<sup>2+</sup>", "$^{2+}$"))
                resume.write(bigskip)

    # with open("../_data/skills.yml") as skl_yaml:
    #     resume.write("\\section{Skills}\n")
    #     skl_data = yaml_load(skl_yaml, Loader=yaml_loader)
    #     for sets in skl_data:
    #         if "Scientific" in str(sets["name"]):
    #             for skills in sets["skills"]:
    #                 resume.write(str(skills["name"]) + midskip)

    resume.write("\\end{resume}")
    resume.write("\\newpage")
    resume.write("\\begin{resume}")

    with open("../_data/publications.yml") as pub_yaml:
        resume.write("\\section{Publications}\n")
        pub_data = yaml_load(pub_yaml, Loader=yaml_loader)
        for paper in pub_data:
            resume.write(paper["authors"] + " ``" + str(paper["title"]).replace(".", ".''")
                         + " \\textit{" + paper["journal"] + "}");
            if "volume" in paper:
                resume.write(" {\\bf " + str(paper["volume"]) + "}")
            resume.write(" (" + str(paper["year"]) + ") "
                         + str(paper["pages"]).replace("&mdash;", "--") + ".")
            if "doi" in paper:
                resume.write(" DOI: \\href{https://doi.org/" + paper["doi"] + "}{"
                             + str(paper["doi"]).replace("_", "\\_") + "}")
            resume.write(midskip)
        resume.write("\n")
        # resume.write("\\vskip-4\\baselineskip\n")

    with open("../_data/recognition.yml") as awd_yaml:
        resume.write("\\section{Recognition}\n")
        awd_data = yaml_load(awd_yaml, Loader=yaml_loader)
        for org in awd_data:
            resume.write("{\\bf " + str(org["name"]).replace("<em>", "\\textit{").replace("</em>", "}") + "}")
            for award in org["awards"]:
                resume.write(midskip)
                resume.write("\\href{" + str(award["url"]) + "}{\\textit{" + str(award["name"]).replace("<em>", "\\textit{").replace("</em>", "}") + "}} "
                             + "\\hfill " + str(award["date"]))
                if "summary" in award:
                    resume.write(lilskip)
                    resume.write(str(award["summary"]).replace('."', ".''").replace('"', '``'))
            resume.write(bigskip)

    with open("../_data/projects.yml") as pro_yaml:
        resume.write("\\section{Projects}\n")
        pro_data = yaml_load(pro_yaml, Loader=yaml_loader)
        for project in pro_data:
            resume.write("\\textit{" + project["role"]
                         + "}, \href{" + project["url"] + "}{" + project["name"] + "}"
                         + "\\hfill " + str(project["start"]) + " to " + str(project["until"]))
            if "summary" in project:
                resume.write(lilskip)
                resume.write(str(project["summary"]).replace("&nbsp;", "~"))

            resume.write(midskip)

    resume.write("\\end{resume}")
    resume.write("\\vskip-2\\baselineskip")
    resume.write("\\newpage")
    resume.write("\\begin{resume}")

    with open("../_data/presentations.yml") as pre_yaml:
        resume.write("\\section{Presentations}\n")
        pre_data = yaml_load(pre_yaml, Loader=yaml_loader)
        for talks in pre_data:
            for talk in talks["presentations"]:
                if "invited" in talk:
                    resume.write("{\\bf Invited:} ")
                resume.write(str(talk["authors"]).rstrip().replace("<u>", "\\textit{").replace("</u>", "}") + ". ``"
                             + str(talk["title"]).replace(".", ".''").replace("&amp;", "\&")  + " "
                             + str(talk["conference"]).replace("&amp;", "\&") + ". " + talk["location"] + ": "
                             + str(talk["date"]) + "." + midskip);

    resume.write("\\end{resume}")

    with open("footer.tex") as footer:
        for line in footer.readlines():
            resume.write(line)
