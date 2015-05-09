OPENSLDIR=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
export CLASSPATH=/usr/local/Cellar/antlr/4.5/antlr-4.5-complete.jar:CLASSPATH
export PYTHONPATH=build/utilities/nsl
export top_srcdir=$(OPENSLDIR)/src
export top_builddir=$(OPENSLDIR)/build
export opennsl_srcdir=$(abspath .)/../OpenNSL/
export BUILDCACHE_CACHEDIR=${HOME}/dev/buildcache

ifeq ($(USE_BUILDCACHE), 1)
BUILDCACHE?=$(OPENSLDIR)/../buildcache/
BUILDCACHE_CACHEDIR?=$(OPENSLDIR)/../make-cache/$(shell basename `/bin/pwd`)
MAKE=$(BUILDCACHE)/buildcache make
else
MAKE=make
endif


test:
	$(MAKE) -C src/utilities
	python src/compile.py -f ~/dev/OpenNSL/include/opennsl/pkt.h
