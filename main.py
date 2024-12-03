import asyncio
import socket

SERVER = 127.0.0.1
PORT = 6000

class UDPClient:
  async def handle_client(data, addr, server_socket):
      print(f"Message received from {addr}: {data.decode()}")
      server_socket.sendto("Message received".encode(), addr)


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER, PORT))
    server_socket.setblocking(False)
    
    loop = asyncio.get_event_loop()

    print("Server UDP was listening on localhost:6000.")

    while True:
        data, addr = await loop.sock_recvfrom(server_socket, 1024)
        await UDPClient.handle_client(data, addr, server_socket)

if __name__ == '__main__':
    asyncio.run(main())
