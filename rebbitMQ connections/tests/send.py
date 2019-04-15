import pika

credentials = pika.PlainCredentials('root', 'toor')
connection = pika.BlockingConnection(pika.ConnectionParameters('165.22.68.42','5672','/',credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')
for i in range (33):
    
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='{"type":"string","body":"%d World!"}'%(i))
    print(" [x] Sent 'Hello World!'")

connection.close()
