all: TKellerPhD.tex TKellerPhD.pdf
.PHONY: TKellerPhD.tex

TKellerPhD.pdf: TKellerPhD.tex
	latexmk -pdf $<

TKellerPhD.tex: synthesizer.py header.tex footer.tex ../_config.yml
	python synthesizer.py
