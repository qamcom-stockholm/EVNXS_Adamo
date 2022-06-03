import types
class Message:
    Content:str
    Sender:str
    Receiver:str
    TimeToLive:int
    CorrelationID:int
    def __init__(self, content:str, sender:str, receiver:str, time_to_live:int, correlation_id:int):
        self.Content = content
        self.Sender = sender
        self.Receiver = receiver
        self.TimeToLive = time_to_live
        self.CorrelationID = correlation_id
#==============================================================================
class Consumer:
    State:Integer  
    # 0: not connected, 1: connected, 2: connected and ready
    # 3: acked
    def __init__(self, name:str, callback:types.FunctionType):  
        self.name = name
        self.callback = callback
        self.State = 0
#==============================================================================
class Queue:
    Name:str
    Durable:bool
    Temporary:bool
    Consumers:List[Consumer]
    def __init__(self, name:str):
        self.Name = name
        self.Consumers = []
        self.Durable = False
        self.Temporary = False
    def add_consumer(self, consumer:Consumer):
        self.Consumers.append(consumer)
    def remove_consumer(self, consumer:Consumer):
        self.Consumers.remove(consumer)
#==============================================================================
class Exchange:
    Type:str    #direct, topic, header, fanout
    Durable:bool
    Queues:List[Queue]
    Name:str
    def __init__(self, name:str):
        self.Name = name
        self.Queues = []

#==============================================================================
class Producer:
    SendingQueue:Queue
    BindingKey:str
    TopicPattern:str
    def __init__(self, queue:Queue, key:str, topic:str):
        self.SendingQueue = queue
        self.BindingKey = key        
        self.TopicPattern = topic

    def send_to(self, message:Message, receiver:str):
        for consumer in self.SendingQueue.Consumers:
            if consumer.name == receiver:
                consumer.callback(message)
                return
        raise Exception("No consumer with name " + receiver)
    def broadcast(self, message:Message):
        for queue in self.Queues:
            for consumer in queue.Consumers:
                consumer.callback(message)
#==============================================================================
class MessageBroker:
    RoundRubin:Boolean
    Queues:List[Queue]
    Producers:List[Producer]
    def __init__(self, round_rubin:Boolean):
        self.RoundRubin = round_rubin
        self.Queues = []
        self.Producers = []

