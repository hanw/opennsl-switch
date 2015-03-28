include ../Make.vars

parser.py: nsl/C.g
	java org.antlr.v4.Tool \
	-o $(TOP_BUILD_DIR)/utilities/nsl \
	-Dlanguage=$(PARSER_LANG) \
	$(TOP_SRC_DIR)/utilities/nsl/C.g

compile:
	$(PYTHON) compile.py -f ~/dev/OpenNSL/include/opennsl/pkt.h
