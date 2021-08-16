#!/bin/bash
gsed -i -e 's/ff1717/e8a0e7/g' season{12,13,14,15,16,17,18,19,20,21,22,23}/*.json
gsed -i -e 's/a0e7e8/ff1717/g' season{12,13,14,15,16,17,18,19,20,21,22,23}/*.json
