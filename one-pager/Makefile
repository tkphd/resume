all: TKellerPhD.pdf
.PHONY: all clean

TKellerPhD.pdf: TKellerPhD.tex
	latexmk -pdf -pdflatex="xelatex -synctex=1 -interaction=errorstopmode" $<

clean:
	latexmk -c
