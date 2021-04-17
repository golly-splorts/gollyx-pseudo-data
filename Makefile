include common.mk

CB := $(shell git branch --show-current)

all:
	@echo "no default make rule defined"

release_mainx:
	@echo "Releasing current branch $(CB) to main"
	scripts/release.sh $(CB) mainx
