#!/bin/bash


# Swap TB bb0000 with DECO e7a0e8
gsed -i -e 's/bb0000/SENTINELSTRING/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/BB0000/SENTINELSTRING/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/e7a0e8/bb0000/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/a0e7e8/bb0000/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/SENTINELSTRING/e7a0e8/g' season{3,4,5,6,7,8,9,10,11}/*.json

# Swap DECO e7a0e8 with AA ff1717
# Swap DECO a0e7e8 with AA ff1717
gsed -i -e 's/e7a0e8/SENTINELSTRING/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/a0e7e8/SENTINELSTRING/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/ff1717/e7a0e8/g' season{3,4,5,6,7,8,9,10,11}/*.json
gsed -i -e 's/SENTINELSTRING/ff1717/g' season{3,4,5,6,7,8,9,10,11}/*.json
