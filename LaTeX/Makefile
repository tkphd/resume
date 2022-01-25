all: TKellerPhD.tex TKellerPhD.pdf
.PHONY: TKellerPhD.tex clean

TKellerPhD.pdf: TKellerPhD.tex
	latexmk -pdf -pdflatex="pdflatex -synctex=1 -interaction=errorstopmode" $<

TKellerPhD.tex: synthesizer.py header.tex footer.tex ../_config.yml ../_data/*.yml
	python synthesizer.py

clean:
	latexmk -c
