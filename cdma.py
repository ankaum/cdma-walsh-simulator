import numpy as np
import csv
import time
import copy

def walsh_mat(ordre):
    walsh = np.array([0.0])
    for i in range(ordre):
        walsh = np.tile(walsh, (2, 2))
        half = 2**i
        walsh[half:, half:] = np.logical_not(walsh[half:, half:])
    return walsh

def antipodeur(mat):
    antipod = copy.deepcopy(mat)
    antipod[antipod == 1] = -1
    antipod[antipod == 0] = 1
    return antipod

def multiplexeur(nbr_users, mat_antipodale, msgs):
    #result = [0] * 16
    packet = mat_antipodale
    for i in range (nbr_users ):
        packet[i] *= msgs[i]
    result = np.sum(packet, axis=0)
    print(packet)
    return result

def demultiplexeur(packet_mux, nbr_users, mat_antipodale):
    dmsgs = [0]*15
    for i in range(nbr_users):
        dmsgs[i] = (np.dot(packet_mux, mat_antipodale[i])) / 16
    return dmsgs

def orderdetector(nbr_users):
    ordre = 0
    flag = 1
    while (flag == 1):
        if (nbr_users<= 2**ordre):
            return ordre
        else:
            ordre +=1

#I will define the data reader function here

print("Plz specify the nbr of users to link:")
nbr_users = int(input())
ordreWalsh = orderdetector(nbr_users)
print("Walsh matrix defined order:", ordreWalsh)
time.sleep(1)
print("Generating the Walsh matrix...")
walshMatrix = walsh_mat(ordreWalsh)
time.sleep(1.69)
print("WalshMAT:")
print(walshMatrix)
time.sleep(1.69)
print("testing if the antipodeur function is working...")
antipodeMat = antipodeur(walshMatrix)
time.sleep(1.69)
print("AntipodWalsh:")
print(antipodeMat)
print("WalshMAT:")
print(walshMatrix)