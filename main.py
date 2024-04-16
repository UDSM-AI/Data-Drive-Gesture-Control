# import os
# import webbrowser
# import threading
# import http.server
# import socketserver
# from src.steer_direction import track_hand

# # Define the directory and port
# dir = "sim/"
# port = 8000

# # Create a simple server
# Handler = http.server.SimpleHTTPRequestHandler

# # Change the working directory to 'sim/'
# os.chdir(dir)

# # Start the server in a new thread
# server_thread = threading.Thread(target=lambda: socketserver.TCPServer(("", port), Handler).serve_forever())
# server_thread.start()

# # Open the web server in the default web browser
# webbrowser.open(f"http://localhost:{port}")

# # Launch the hand tracking
# track_hand()

# # When done, shutdown the server
# socketserver.TCPServer(("", port), Handler).shutdown()


# #######################################################################3
import webbrowser
from src.steer_direction import track_hand

# Open the web page in the default web browser
webbrowser.open("http://slowroads.io")

# Launch the hand tracking
track_hand()