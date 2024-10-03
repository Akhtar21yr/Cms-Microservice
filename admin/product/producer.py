import pika, json

params = pika.URLParameters('amqps://jkxwunkb:UlDNXCjY--u5M-eiTaLCZID7hhdWX3JY@rattlesnake.rmq.cloudamqp.com/jkxwunkb')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)