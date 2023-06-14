import pika

# Fungsi callback untuk menangani pesan yang diterima
def callback(ch, method, properties, body):
    print("Menerima pesan:", body)

# Buat koneksi ke RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Buat antrian dengan nama 'hello' (jika belum ada)
channel.queue_declare(queue='hello')

# Daftarkan fungsi callback ke antrian 'hello'
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# Mulai konsumsi pesan
print("Menunggu pesan...")
channel.start_consuming()
