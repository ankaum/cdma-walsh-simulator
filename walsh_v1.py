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
antipod_mat =  np.delete(antipod, (0), axis = 0)
def multiplex(nbr_users, antipod_mat, msgs):
    #result = [0] * 16
    print("multip antipod:")
    print(antipod_mat)
    packet = antipod_mat
    for i in range (nbr_users ):
        packet[i] *= msgs[i]
    result = np.sum(packet, axis=0)
    print(packet)
    return result

res = multiplex(3, antipod_mat, msgs)
print(res)

antipoddemux = walsh_mat(4)
antipode = antipoddemux
antipode[antipode == 1] = -1
antipode[antipode == 0] = 1
antipod_mate =  np.delete(antipode, (0), axis = 0)
print("antipodlast")
print(antipod_mate)
def demux(muxpack, antipod_mate, nbrusers):
    dmsgs = [0]*15
    for i in range(nbrusers):
        dmsgs[i] = (np.dot(muxpack, antipod_mate[i])) / 16
    return dmsgs

demuxmsg= demux(res, antipod_mate, user_nbr)
print(demuxmsg)