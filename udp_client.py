class UDPClient:
  async def handle_client(data, addr, server_socket):
      print(f"Message received from {addr}: {data.decode()}")
      server_socket.sendto("Message received".encode(), addr)
