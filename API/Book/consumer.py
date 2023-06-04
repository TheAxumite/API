import time
import sys
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

counter = 0
average = 0
list = 0

class SocketConsumer(AsyncJsonWebsocketConsumer):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_size = 0
        self.elapsed_time=0
        self.last_time = time.time()

    

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print(self.elapsed_time)
        current_time = time.time()
        self.elapsed_time = self.elapsed_time + current_time - self.last_time

        
        global counter
        global average
        global list


        content = json.loads(text_data)
        self.data_size += sys.getsizeof(content) / 1024  # Convert to KB

        counter += 1

        packet_size = sys.getsizeof(text_data) / 1024  # Size in KB
        list += packet_size
        average = list / counter

        # If one second has passed, calculate and print data rate
        if self.elapsed_time >= 1:
            data_rate = self.data_size / self.elapsed_time  # KB/s
            print(f"KB Transmitted per second: {data_rate}")
            self.data_size = 0
            self.last_time = current_time
     
        print(self.elapsed_time)
        print(content[0]['Frame'])
        print(f"Packet Size: {packet_size}")
        print(f"Average KB per transaction: {average}")
  
        response_content = {'message': f"Received Frame {content[0]['Frame']}"}
        await self.send_json(content=response_content)
