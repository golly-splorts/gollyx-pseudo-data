#!/bin/bash


# Swap TB bb0000 with DECO e7a0e8
gsed -i -e 's/bb0000/SENTINEL/g' season{0,1,2}/*.json
gsed -i -e 's/BB0000/SENTINEL/g' season{0,1,2}/*.json
gsed -i -e 's/e7a0e8/bb0000/g' season{0,1,2}/*.json
gsed -i -e 's/SENTINEL/e7a0e8/g' season{0,1,2}/*.json

# Swap DECO e7a0e8 with AA ff1717
gsed -i -e 's/e7a0e8/SENTINEL/g' season{0,1,2}/*.json
gsed -i -e 's/ff1717/e7a0e8/g' season{0,1,2}/*.json
gsed -i -e 's/SENTINEL/ff1717/g' season{0,1,2}/*.json
