from array import array
import numpy as np

def walsh_mat(ordre):
    walsh = np.array([0])
    for i in range(ordre):
        walsh = np.tile(W, (2, 2))
        half = 2**i
        walsh[half:, half:] = np.logical_not(walsh[half:, half:])
    return walsh
    
print("Walsh code 16 is:")
matrice = walsh_mat(4)
print(matrice)
antipod = matrice
antipod[antipod == 1] = -1
antipod[antipod == 0] = 1
print("Antipod 16 users:")
print(antipod)

print("input nbr of users (max 16):")
user_nbr = int(input())

def multiplex(nbr_users, antipod, msgs):
    result = [0] * 16
    packet = antipod
    for i in range (nbr_users - 1):
        packet[i] *= msgs[i]
    result = np.sum(packet, axis=0)