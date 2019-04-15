import pika

credentials = pika.PlainCredentials('root', 'toor')
connection = pika.BlockingConnection(pika.ConnectionParameters('165.22.68.42','5672','/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()