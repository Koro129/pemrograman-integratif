from kafka import KafkaConsumer

# Inisialisasi KafkaConsumer
consumer = KafkaConsumer(
    'nama_topik',
    bootstrap_servers='localhost:9092',
    group_id='group_id',
    auto_offset_reset='earliest'
)

# Membaca pesan dari topik
for message in consumer:
    pesan = message.value.decode('utf-8')
    print(f"Menerima pesan: {pesan}")

# Menutup koneksi KafkaConsumer
consumer.close()
