#!/bin/bash
gsed -i -e 's/ff1717/ABRACADABRA/g' season{12,13,14,15,16,17,18,19,20,21,22,23}/*.json
gsed -i -e 's/bb0000/ff1717/g' season{12,13,14,15,16,17,18,19,20,21,22,23}/*.json
gsed -i -e 's/ABRACADABRA/bb0000/g' season{12,13,14,15,16,17,18,19,20,21,22,23}/*.json
