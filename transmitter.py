import logging
import pickle
import socket
import sys

import numpy as np

import utils

# ? Configure logging
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


class UserEncode:
    """Class to contain encoding and mixing methods for CDMA"""

    def __init__(self, uId, code):

        # * uId is just for logging purposes
        self.uId = uId
        self.code = np.reshape(code, (1, -1))

    def encode(self, data):
        """Encodes data with code of user

        Args:
                data (ndarray): 1D data array of symbols to be transmitted

        Returns:
                ndarray: Encoded data
        """
        return np.dot(data.T, self.code)

    def mix(self, data, channel):
        """adds current encoded data to channel

        Args:
                data (ndarray): multi-dimensional encoded data array
                channel (ndarray): multi-dimensional channel array
        Returns:
                ndarray: updated channel
        """
        d = self.encode(data)
        return channel + d


def cdma_channel(no_of_users, messages):
    """
    This function generates the final signal to be sent in the channel
    after CDMA with message and codes

    Args:
            no_of_users (int): number of users that send data in the channel
            messages (list): list of messages correspoding to each user

    Returns:
            channel_data (ndarray): 2D array containing all data to be sent in the channel
    """

    # ? Find longest message and pad other messages
    max_len = len(max(messages, key=len))
    equilen_messages = [msg.ljust(max_len, " ") for msg in messages]

    # ? Generate Walsh Matrix
    walsh = np.array(utils.walsh_code_generator([[-1]], no_of_users), dtype=int)

    # ? Convert string to symbol array
    symbols = list((map(utils.text2binarr, equilen_messages)))

    # ? Create Channel matrix
    channel = np.zeros((max_len * 8, walsh.shape[0]), dtype=int)

    # ? Create user with uid and their respective walsh code
    for i in range(no_of_users):
        u = UserEncode(uId=i, code=walsh[i])
        a = np.array(symbols[i])

        logging.debug("Symbols sent by User %d:", u.uId)
        logging.debug(symbols[i])

        # ? Encodes the data with code and updates the channel data
        channel = u.mix(a, channel)

    return channel


if __name__ == "__main__":

    # ? Connect to receiver and send channel data
    # * Connection type is IPv4 and TCP

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostname(), 3300))

    no_of_users = int(sys.argv[1])
    messages = []

    for i in range(no_of_users):
        cur_message = input(f"Enter message for User {i}: ")
        messages.append(cur_message)

    logging.info("\nNO_OF_USERS: {0}\nMESSAGES: {1}".format(no_of_users, messages))
    data = cdma_channel(no_of_users, messages)

    logging.debug(f"Channel Matrix:\n{data}")

    sock.sendall(pickle.dumps(data))
    sock.close()
