import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))

s.send(b'GET / HTTP/1.1\r\nHosts: www.sina.com\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d= s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

date = b''.join(buffer)

s.close()

header, html = date.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.com.html', 'wb') as f:
    f.write(html)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connecting......')

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break

    sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)



while True:

    sock, addr = s.accept()

    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

