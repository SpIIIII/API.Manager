import time
import pika

credentials = pika.PlainCredentials('root', 'toor')
connection = pika.BlockingConnection(pika.ConnectionParameters('165.22.68.42','5672','/',credentials))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body))
    time.sleep( body.count(b'.') )
    print (" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()