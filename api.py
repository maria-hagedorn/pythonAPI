from http.server import BaseHTTPRequestHandler, HTTPServer

#import socketserver
#import json

PORT = 8000
HOSTNAME = "localhost"

content = ["test", "something", "to", "see", "it", "work!"]

def listToString(s: str) -> str:
    str = "["
 
    for i in range(0, len(s)):
        str += s[i]
        if (i != (len(s) - 1)): str += ", "

    str += "]"
    return str


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        # Get all
        if path == "/":
            response(self, 200)
        
        # Get index
        else:
            index = getIndex(self)
            
            if index >= 0 and index < len(content):
                response(self, 200, index)
            else:
                response(self, 405)
                return


    def do_POST(self):
        # Append content
        post_body = rawBody(self)
        content.append(post_body)

        response(self, 200)


    def do_PUT(self):
        index = getIndex(self)

        if index >= 0 and index < len(content):
            content[index] = rawBody(self) # Update value at index
            response(self, 200, index)

        else:
            response(self, 405)
            return


    def do_DELETE(self):

        index = getIndex(self)

        if index >= 0 and index < len(content):
            # Delete value at index
            content.pop(index)
            response(self, 200, index)
        else:
            response(self, 405)
            return  


######### HELPER FUNCTIONS #########

def getIndex(self):
    path = self.path


    # get index
    try:
        index = int(path[1:])
        return index
    except ValueError:
        self.send_response(405)
        self.end_headers()
        return

def response(self, code, index=-1):
    if(code < 300):
        self.send_response(code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        writeToBody(self, index)
    else:
        self.send_response(code)
        self.end_headers()

def writeToBody(self, index):
    if(index == -1):
        self.wfile.write(bytes(listToString(content), "utf-8"))
    else:
        self.wfile.write(bytes(content[index], "utf-8"))   

def rawBody(self):
    content_len = int(self.headers.get('Content-Length'))
    return self.rfile.read(content_len).decode("utf-8")


        


if __name__ == "__main__":
    webServer = HTTPServer((HOSTNAME, PORT), MyServer)
    print("Server started http://%s:%s" % (HOSTNAME, PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt: 
        pass

    webServer.server_close()
    print("Server stopped.")
