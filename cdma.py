import numpy as np

def walsh_mat(ordre):
    walsh = np.array([0.0])
    for i in range(ordre):
        walsh = np.tile(walsh, (2, 2))
        half = 2**i
        walsh[half:, half:] = np.logical_not(walsh[half:, half:])
    return walsh

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

print 
