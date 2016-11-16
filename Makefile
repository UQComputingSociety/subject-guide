TEX = pdflatex -interaction=nonstopmode -halt-on-error -output-directory _build

all : subject-guide

subject-guide : tex/main.tex
	cd tex && mkdir _build; $(TEX) main.tex && $(TEX) main.tex && $(TEX) main.tex && $(TEX) main.tex

clean :
	rm -rf tex/_build