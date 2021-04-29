# all (přeloží projekt - včetně programu pro profiling)
# pack (zabalí projekt tak, aby mohl být odevzdán)
# clean (smaže všechny soubory, co nemají být odevzdány)
# test (spustí testy matematické knihovny)
# doc (spustí generování dokumentace)
# run (spustí program)
# profile (spustí překlad programu pro výpočet směrodatné odchylky na profiling)

all: profile

pack:
	zip ivs_projekt.zip * # TODO:

clean:
	# todo

test:
	python3 -m unittest tests/test_math_unittest.py

doc:
	doxygen

run: # todo: add all requirements
	python3 calc.py

profile: # todo
