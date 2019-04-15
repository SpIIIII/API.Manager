import sys
import pika
import time 

credentials = pika.PlainCredentials('root', 'toor')
connection = pika.BlockingConnection(pika.ConnectionParameters('165.22.68.42','5672','/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_qos(prefetch_count=1)

message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range (20):
    time.sleep(3)
    if i%2==0:
        channel.basic_publish(exchange='',
                            routing_key='hello',
                            body='.....{}'.format(i),
                            properties=pika.BasicProperties(
                            delivery_mode = 2, # make message persistent
                            )
                      )
        print(" [x] Sent %r" % (message))
    else:
        channel.basic_publish(exchange='',
                            routing_key='hello',
                            body=f'Boo{i}')
        print(" [x] Sent %r" % message)

connection.close()
