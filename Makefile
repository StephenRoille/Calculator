
clean: doc-clean
	rm -f .coverage
	rm -f *.exe
	rm -f *.pyz
	rm -rf .hypothesis
	rm -rf .pyinstaller
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf shapr/.mypy_cache
	rm -rf shapr/__pycache__
	rm -rf tests/__pycache__

# ====
# DOCS
# ====

# PREPARE
# -------
doc-checks: doc-spelling doc-links

doc-clean:
	rm -rf docs/__pycache__
	rm -f docs/README.rst
	find ./docs/api -mindepth 1 -maxdepth 1 -type d -exec rm -r {} +
	cd docs && make clean

doc-links: doc-readme
	cd docs && make linkcheck

doc-readme:
	pandoc -o docs/README.rst README.md

doc-spelling: doc-readme
	cd docs && make spelling

doc-prepare: doc-clean doc-readme

doc-prepare-with-checks: doc-clean doc-readme doc-checks

# FAST
# ----
doc-live: doc-prepare
	sphinx-autobuild docs docs/_build/html \
	--ignore *.pdf \
	--ignore *.html \
	--ignore *.pyc \
	--ignore *.png \
	--ignore *.svg \
	--ignore *.dll \
	--ignore *.zip \
	--open-browser \
	--delay 5 \
	--watch src

doc-html: doc-readme
	cd docs && make html

doc-open:
	chrome ./docs/_build/html/index.html

# WITH CHECKS
# -----------
doc-live-with-checks: doc-prepare-with-checks
	sphinx-autobuild docs docs/_build/html \
	--ignore *.pdf \
	--ignore *.html \
	--ignore *.pyc \
	--ignore *.png \
	--ignore *.svg \
	--ignore *.dll \
	--ignore *.zip \
	--open-browser \
	--delay 5 \
	--watch src

doc-html-with-checks: doc-prepare-with-checks
	cd docs && make html


# =========
# PACKAGING
# =========
exe:
	pyinstaller \
	--noconfirm \
	--distpath .pyinstaller/dist \
	--workpath .pyinstaller/build \
	calculator.spec

installer-win64: exe
	makensis installer-win64.nsi
