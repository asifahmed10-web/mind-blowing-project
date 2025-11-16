# socket_server.py

import socket
import time
from eeg_reader import EEGReader
from interpreter import DreamInterpreter

def run_server(host="127.0.0.1", port=65432):
    eeg = EEGReader()
    interpreter = DreamInterpreter()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"Server listening on {host}:{port}")
    conn, addr = server.accept()
    print("Connected by", addr)

    try:
        while True:
            signals = eeg.read()
            emotion = interpreter.interpret(signals)
            msg = emotion.encode("utf-8")
            conn.sendall(msg)
            print("Sent:", emotion)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping server...")
    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    run_server()
