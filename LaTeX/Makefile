TKellerPhD.pdf: TKellerPhD.tex
	latexmk -pdf $<

.PHONY: TKellerPhD.tex
TKellerPhD.tex: synthesizer.py header.tex footer.tex
	python synthesizer.py
