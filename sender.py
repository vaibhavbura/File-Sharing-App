import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import tkinter as tk
from tkinter import ttk
import os

PORT = 8010

desktop = os.path.join(os.path.expanduser('~'), 'Desktop/Share')
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
except Exception as e:
    print("Error getting IP address:", e)
    IP = "http://localhost:" + str(PORT)
finally:
    s.close()

url = pyqrcode.create(IP)
url.svg("myqr.svg", scale=8)

def open_browser():
    webbrowser.open('myqr.svg')

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        print("Type this in your Browser:", IP)
        print("or Use the QR Code")
        httpd.serve_forever()

root = tk.Tk()
root.title("HTTP Server")
root.geometry("400x200")

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 16))

label = ttk.Label(root, text="File Sharing App")
label.pack(pady=10)

qr_button = ttk.Button(root, text="Open QR Code", command=open_browser)
qr_button.pack(pady=5)

start_button = ttk.Button(root, text="Start Server", command=start_server)
start_button.pack(pady=5)

root.mainloop()
