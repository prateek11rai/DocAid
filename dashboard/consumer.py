from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
    
    async def disconnect(self,close_code):
        
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val = datapoint['value']
        val2 = datapoint['value2']
        val3 = datapoint['value3']
        val4 = datapoint['value4']
        print('>>>>>',text_data)
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':val,
                'value2':val2,
                'value3':val3,
                'value4':val4
            }
        )
    
    async def deprocessing(self,event):
        valOther=event['value']
        valOther2=event['value2']
        valOther3=event['value3']
        valOther4=event['value4'] 
        #anomaly detection code here
        await self.send(text_data=json.dumps({'value':valOther,'value2':valOther2,'value3':valOther3,'value4':valOther4}))
