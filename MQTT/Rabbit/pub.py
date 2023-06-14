# rabbitMQ Service - start
# http://localhost:15672/#/
import pika

# Buat koneksi ke RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Buat antrian dengan nama 'hello'
channel.queue_declare(queue='hello')

# Kirim pesan "Hello, World!" ke antrian 'hello'
channel.basic_publish(exchange='', routing_key='hello', body='Hello, World!')
print("Pesan terkirim!")

# Tutup koneksi
connection.close()
