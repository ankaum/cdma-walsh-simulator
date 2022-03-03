

## CDMA Simulation
 Simulation of Code Division Multiple Access protocol using Walsh codes.

 ## Overview
 Walsh Codes are mostly used in the orthogonal codes of CDMA transmissions. These codes correspond to lines of a special   square matrix called the Hadamard matrix. For a set of Walsh codes of length N, it consists of n lines to form a square matrix of n*n Walsh code. Walsh matrices are just Hadamard matrices and can be created using the given formula, given an initial matrix. This is also why Walsh codes are also called Walsh-Hadamard codes.

 The program encodes the messages included in the csv file with the respective walsh codes and generates the signal to be sent in the channel. The same signal will be decoded by using the same walsh matrix and the messages will be stored in another csv file.

 The goal of this simulation is to demonstrate the distinguishing features of CDMA that are key to spread spectrum transmission technologies

## Dependencies
- Python version >=`2.7`
- Pandas
- Numpy

## How to run
- `python cdma_walsh_v2.py`
-  You can test the program by modifying the messages in the`.csv`file
