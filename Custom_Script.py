import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random
import json

import websocket

ws = websocket.WebSocket()
ws.connect(r'ws://localhost:8000/ws/polData/')
for i in range(1000):
    time.sleep(5)
    ws.send(json.dumps({'value':random.randint(100,150),'value2':random.randint(1,50),'value3':random.randint(50,100),'value4':random.randint(150,200)}))
