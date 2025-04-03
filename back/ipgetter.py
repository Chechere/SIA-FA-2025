from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, setdefaulttimeout, error

def get_local_ip():
    google_dns = "8.8.8.8"
    port = 80

    try:
        connection = socket(AF_INET, SOCK_DGRAM)
        connection.connect((google_dns, port))
        local_ip_address = connection.getsockname()[0]
        return local_ip_address
    except Exception as e:
        return socket.gethostbyname(socket.gethostname())
    finally:
        connection.close()
