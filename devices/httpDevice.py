from http.server import BaseHTTPRequestHandler,HTTPServer
from threading import Thread

class httpDevice(Thread, HTTPServer):
    def __init__(self, port):
        Thread.__init__(self)
        HTTPServer.__init__(self, ('', port), httpDeviceHandler)
        self.start()
        self.eventListeners = []

    def run(self):
        self.serve_forever()
        
    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)

    def suscribe(self, listener):
        self.eventListeners += [listener]

    def stop(self):
        self.server_close()

class httpDeviceHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super(httpDeviceHandler, self).__init__(request, client_address, server)
        
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.buttons = [
            ["AccessRequest","RFID Entrada"],
            ["EntranceBarrierOpens","Barrera entrada cortada"],
            ["EntranceBarrierCloses","Barrera entrada liberada"],
            ["EntranceGateCloses","Porton entrada cerrado"],
            ["PumpAccessRequest","RFID Surtidor"],
            ["PumpCloses","Surtidor cerrado"],
            ["ExitRequest","Petición de salida"],
            ["ExitBarrierOpens","Barrera salida cortada"],
            ["ExitBarrierCloses","Barrera salida liberada"],
            ["ExitGateCloses","Porton salida cerrado"],
        ]

        command = self.path.split("/")
        
        if len(command) > 2 and command[1] == "action":
            self.server.raiseEvent(command[2], command[3:])

        buttons = ""
        for btn in self.buttons:
            buttons += '<div class="btn"><a class="button" href="/action/{0}">{1}</a></div>'.format(*btn)

        self.wfile.write(bytes("""
        <html><head><title>Petromatic</title></head>
            <body>
                <p>Path: {0}</p>
                <style>
                    a.button {{
                        -webkit-appearance: button;
                        -moz-appearance: button;
                        appearance: button;

                        text-decoration: none;
                        color: initial;
                        padding: 5px;
                    }}
                    .btn {{
                        display: block;
                        margin: 5px;
                    }}
                </style>

                {1}

            </body>
        </html>
        
        """.format(self.path, buttons), "utf-8"))

    def log_message(self, format, *args):
            return