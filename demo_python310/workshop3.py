# Step 1: Define User Roles with Structured Pattern Matching
import socket
import asyncio

def validate_user_access(user_profile: dict | None) -> str:
    """
    Validates user access based on their role and subscription status.
    Returns an access message depending on the user profile structure.
    """
    if user_profile is None:
        raise ValueError("Error: Missing profile data.")
    
    match user_profile:
        case {"role": "admin", "name": str(name)}:
            return f"Access granted to all resources for Admin {name}."
        case {"role": "member", "name": str(name), "subscription_status": True}:
            return f"Access granted to member resources for {name}."
        case {"role": "member", "name": str(name), "subscription_status": False}:
            return f"Limited access: {name}, please renew your subscription."
        case {"role": "guest", "name": str(name)}:
            return f"View-only access granted for Guest {name}."
        case _:
            return "Access denied: unknown role"


## Step 2: Start socket server
async def start_access_server(host:str, port:int, handler):
    """
    Starts an asynchronous server to handle incoming access requests.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen()
    server_sock.setblocking(False)

    loop = asyncio.get_running_loop()
    print(f"Server running on {host}:{port}...")

    while True:
        client_sock, _ = await loop.sock_accept(server_sock)
        
        #Create a StreamReader
        reader = asyncio.StreamReader()
        #Create a StreamReaderProtocol to bind the reader to the client socket
        protocol = asyncio.StreamReaderProtocol(reader)
        #Use connect_accepted_socket to integrate the socket and protocol
        transport, _ = await loop.connect_accepted_socket(lambda: protocol, client_sock)
        
        # create a StreamWriter
        writer = asyncio.StreamWriter(transport, protocol, reader, loop)
        # Start processing the request
        asyncio.create_task(handler(reader, writer))

async def process_access_request(reader, writer):
    """
    Processes an access request from a client. Reads the user profile,
    validates access, and sends back a response based on the profile data.
    """
    data = await reader.read(1024)
    user_profile = eval(data.decode())  # Assume data is received as a dictionary (for simplicity)
    
    try:
        # Validate user access based on the profile data
        response = validate_user_access(user_profile)
    except ValueError as e:
        # Handle missing fields or invalid data
        response = f"Validation error: {e}"
    
    # Send the access response back to the client
    writer.write(response.encode())
    await writer.drain()
    writer.close()

asyncio.run(start_access_server("localhost", 8083, process_access_request))