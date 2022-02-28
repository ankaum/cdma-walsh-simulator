from array import array
import numpy as np

def walsh_mat(ordre):
    walsh = np.array([0])
    for i in range(ordre):
        walsh = np.tile(walsh, (2, 2))
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
#antipod = antipod.astype(float)

print("input nbr of users (max 16):")
user_nbr = int(input())
msgs = [0]*16
msgs[0]= 2
msgs[1]= 3
msgs[2] = 4
print(msgs)
antipod_mat =  antipod
def multiplex(nbr_users, antipod_mat, msgs):
    #result = [0] * 16
    print("multip antipod:")
    print(antipod_mat)
    i = 0
    packet = antipod_mat
    for i in range (nbr_users ):
        packet[i] *= msgs[i]
    result = np.sum(packet, axis=0)
    print(packet)
    return result

res = multiplex(3, antipod_mat, msgs)
print(res)
print("antipodlast")
print(antipod)
"""
def demux(muxpack, antipod):
    dmsgs = [0]*16
    for i in range(16):
        dmsgs[i] = (np.dot(muxpack, antipod[:][i])) / 16
    return dmsgs

demuxmsg= demux(res, antipod)
print(demuxmsg)
"""