# .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
# .\bin\windows\kafka-server-start.bat .\config\server.properties

from kafka import KafkaProducer

# Inisialisasi KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Topik yang akan digunakan
topic = 'nama_topik'

# Pesan yang akan dikirimkan
pesan = 'Halo, ini pesan lagi dari publisher!'

# Mengirim pesan ke topik
future = producer.send(topic, pesan.encode('utf-8'))

# Menunggu konfirmasi pesan terkirim
try:
    record_metadata = future.get(timeout=10)
    print(f"Pesan berhasil terkirim ke topik '{record_metadata.topic}' pada partisi {record_metadata.partition}, offset {record_metadata.offset}")
except Exception as e:
    print(f"Terjadi kesalahan saat mengirim pesan: {str(e)}")

# Menutup koneksi KafkaProducer
producer.close()
