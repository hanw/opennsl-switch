export CLASSPATH=/usr/local/Cellar/antlr/4.4/antlr-4.4-complete.jar:CLASSPATH
export top_srcdir=$(abspath .)/src
export top_builddir=$(abspath .)/build

test:
	make -C src/utilities
