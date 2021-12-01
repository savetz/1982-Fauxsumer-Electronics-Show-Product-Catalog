#!/bin/sh
python3 generatepages.py && pandoc pages-output.md --include-before-body cover.tex -f gfm -H chapterbreak.tex --toc --toc-depth 1 -V toc-title="Featured Products" -V geometry:margin=2cm -V monofont="Atari Classic Chunky" -V mainfont="SpaceMono Nerd Font Mono" --pdf-engine=xelatex -o book.pdf
