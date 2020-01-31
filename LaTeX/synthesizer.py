 # -*- coding: utf-8 -*-

from yaml import load as yaml_load

with open("TKellerPhD.tex", "w") as resume:
    with open("header.tex") as header:
        for line in header.readlines():
            resume.write(line)

    with open("../_data/experience.yml") as exp_yaml:
        resume.write("\\section{Experience}\n")
        exp_data = yaml_load(exp_yaml)
        for company in exp_data:
            if len(company["name"]) > 20:
                resume.write("{\\bf \href{" + company["home"] + "}{" + company["name"] + "}}\\\\\n ")
                resume.write("\\rightline{\href{" + company["url"] + "}{" + company["department"] + ", " + company["location"] + "}}\\\\\n ")
            else:
                resume.write("{\\bf \href{" + company["home"] + "}{" + company["name"] + "}}")
                resume.write("\hfill \href{" + company["url"] + "}{" + company["department"] + ", " + company["location"] + "}\\\\\n ")
            for position in company["positions"]:
                resume.write(position["title"] + " \hfill " + position["start"] + " to " + position["until"] + "\\\\\n ")
                if "summary" in position:
                    resume.write("[0.25\\baselineskip]\n")
                    resume.write(str(position["summary"]).replace("&times;", "$\\times$") + "\n ")

    with open("../_data/education.yml") as edu_yaml:
        resume.write("\\section{Education}\n ")
        edu_data = yaml_load(edu_yaml)
        for school in edu_data:
            resume.write("{\\bf \href{" + school["url"] + "}{" + school["name"] + "}} \\hfill " + school["location"] + "\\\\\n ")
            for degree in school["degrees"]:
                # resume.write("\href{" + degree["url"] + "}{" + degree["department"] + "}\\\\\n ")
                resume.write(degree["name"] + " in " + degree["field"] + "\\hfill " + str(degree["start"]) + " to " + str(degree["until"]) + "\\\\\n ")
                if "thesis" in degree:
                    resume.write("Thesis: \\emph{" + degree["thesis"] + "}\\\\\n ")
                if "summary" in degree:
                    resume.write("[0.25\\baselineskip]\n")
                    resume.write(str(degree["summary"]).replace("<sup>2+</sup>", "$^{2+}$") + "\n ")

    with open("../_data/skills.yml") as skl_yaml:
        resume.write("\\section{Skills}\n")
        skl_data = yaml_load(skl_yaml)
        for sets in skl_data:
            if "Scientific" in str(sets["name"]):
                for skills in sets["skills"]:
                    resume.write(skills["name"] + "\\\\[0.25\\baselineskip]\n")

    with open("../_data/publications.yml") as pub_yaml:
        resume.write("\\section{Publications}\n")
        pub_data = yaml_load(pub_yaml)
        for paper in pub_data:
            resume.write(paper["authors"] + " ``" + str(paper["title"]).replace(".", ".''")  + " \\emph{" + paper["journal"] + "}");
            if "volume" in paper:
                resume.write(" {\\bf " + str(paper["volume"]) + "}")
            resume.write(" (" + str(paper["year"]) + ") " + str(paper["pages"]).replace("&mdash;", "--") + ".")
            if "doi" in paper:
                resume.write(" DOI: \\href{https://doi.org/" + paper["doi"] + "}{" + str(paper["doi"]).replace("_", "\\_") + "}")
            resume.write("\\\\[0.25\\baselineskip]\n")
        # resume.write("\\vskip-4\\baselineskip\n")

    with open("../_data/presentations.yml") as pre_yaml:
        resume.write("\\section{Presentations}\n")
        pre_data = yaml_load(pre_yaml)
        for talks in pre_data:
            for talk in talks["presentations"]:
                if "invited" in talk:
                    resume.write("Invited: ")
                resume.write(str(talk["authors"]).rstrip().replace("<u>", "\\emph{").replace("</u>", "}") + ". ``" + str(talk["title"]).replace(".", ".''").replace("&amp;", "\&")  + " " + str(talk["conference"]).replace("&amp;", "\&") + ". " + talk["location"] + ": " + talk["date"] + ".\\\\[0.25\\baselineskip]\n");
            resume.write("\\vskip-2\\baselineskip\n")

    with open("footer.tex") as footer:
        for line in footer.readlines():
            resume.write(line)
