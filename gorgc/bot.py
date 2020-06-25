import socket
import logging
from emoji import demojize


logging.basicConfig(level=logging.DEBUG,
                    format= '%(message)s', #'%(asctime)s
                    #datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'StreamOfNonsense'
token = 'oauth:obia7ie7ceojn0mzra1cmwuyaited6'
channel = '#gorgc'


def main():
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))



    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                # sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                logging.info(demojize(resp))

    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()