import numpy as np
import time
import copy
import pandas as pd
import array

def walsh_mat(ordre):
    walsh = np.array([0.0])
    for i in range(ordre):
        walsh = np.tile(walsh, (2, 2))
        half = 2 ** i
        walsh[half:, half:] = np.logical_not(walsh[half:, half:])
    return walsh

def antipodeur(mat):
    antipod = copy.deepcopy(mat)
    antipod[antipod == 1] = -1
    antipod[antipod == 0] = 1
    return antipod

def multiplexeur(nbr_users, mat_antipodale, msgs):
    #result = [0] * 16
    packet = copy.deepcopy(mat_antipodale)
    for i in range (nbr_users ):
        packet[i] *= msgs[i]
    result = np.sum(packet, axis=0)
    return result

def demultiplexeur(nbr_users, mat_antipodale, packet_mux,):
    dmsgs = [0.0] * nbr_users
    for j in range(nbr_users):
        dmsgs[j] = ((np.dot(packet_mux, mat_antipodale[j])) / nbr_users)
    return dmsgs

def orderdetector(nbr_users):
    ordre = 0
    flag = 1
    while (flag == 1):
        if (nbr_users<= 2 ** ordre):
            return ordre
        else:
            ordre +=1

#AutoTransmitting via csv packets

df = pd.read_csv("dataToTransmit.csv")
print("The dataframe to transmit, each line represents a user:")
print(df)
data = df.to_numpy()
data = np.transpose(data)
time.sleep(1.69)
print("The data to transfer is listed below.")
print("Every row represents a timeframe")
print(data)
time.sleep(1.69)
nbr_users = len(data[0])
print("The number of users to commute is ", len(data[0]))
time.sleep(0.69)
ordreWalsh = orderdetector(nbr_users)
print("Walsh matrix defined order:", ordreWalsh)
time.sleep(0.69)
print("Generating the Walsh matrix...")
walshMatrix = walsh_mat(ordreWalsh)
time.sleep(1.69)
print("WalshMAT:")
print(walshMatrix)
print("Testing if the antipodeur function is working...")
antipodeMat = antipodeur(walshMatrix)
time.sleep(1.69)
print("AntipodWalsh:")
print(antipodeMat)

time.sleep(1.69)
spreadedSignal = []
receivedData = []
print(len(data))
#print(data)
for i in range(len(data)):
    print(i)
    spreadedSignal.append(multiplexeur(nbr_users, antipodeMat, data[i]))
    receivedData.append(demultiplexeur(nbr_users, antipodeMat, spreadedSignal[i]))
receivedData = np.array(receivedData)
print("Received data:")
print(receivedData)
receivedData = np.transpose(receivedData)
time.sleep(1.69)
receivedDf = pd.DataFrame(receivedData, columns = df.columns)
receivedDf = receivedDf.round(decimals = 2)
print("DF to export:")
print(receivedDf)
time.sleep(1.69)
receivedDf.to_csv("receivedData.csv", index = False)
print("The received dataframe has been exported to \"receivedData.csv\"")

"""
print(np.array(receivedData[1]))
print(np.array(receivedData[2]))
print(np.array(receivedData[3]))
print(np.array(receivedData[4]))
print(np.array(receivedData[5]))
print(np.array(receivedData[6]))
"""

'''
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

msg = [0.0] * len(walshMatrix[0])
msg[0] = 69.0
msg[1] = 420.0
msg[2] = 65.0
msg[3] = 1.5

spreadedSignal = multiplexeur(nbr_users, antipodeMat, msg)
print("Total spreaded signal of all users:")
time.sleep(1.69)
print(spreadedSignal)

orginal_msgs = demultiplexeur(nbr_users, antipodeMat, spreadedSignal)
print("Received msgs (demux):")
time.sleep(1.69)
print(orginal_msgs)
print("Original msgs:")
print(msg)
'''