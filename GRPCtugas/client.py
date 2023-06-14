import grpc
import class_pb2
import class_pb2_grpc

# Inisialisasi channel untuk gRPC client
channel = grpc.insecure_channel('localhost:50051')

# Membuat stub untuk ClassService
stub = class_pb2_grpc.ClassServiceStub(channel)

# Fungsi untuk menampilkan semua kelas
def GetAllClasses():
    # Membuat request dengan Empty protobuf message
    request = class_pb2.Empty()

    # Memanggil method GetAllClasses dari stub
    response = stub.GetAllClasses(request)

    # Menampilkan data kelas yang diterima dari server
    print("=== List Kelas ===")
    for class_ in response.classes:
        print(f'ID: {class_.id}')
        print(f'Nama: {class_.name}')
        print(f'Lokasi Kelas: {class_.location}\n')

# Fungsi untuk menambahkan kelas baru
def AddClass():
    print("=== Tambah Kelas ===")
    id = input("Masukkan ID kelas: ")
    name = input("Masukkan nama kelas: ")
    location = input("Masukkan lokasi kelas: ")

    # Membuat instance protobuf message untuk request
    request = class_pb2.Class(
        id=id,
        name=name,
        location=location
    )

    # Mengirim request ke server menggunakan stub
    response = stub.AddClass(request)
    print(f"Kelas dengan ID {response.id} telah ditambahkan.")



# Fungsi untuk mengedit kelas
def EditClass():
    # Membuat instance EditClassRequest protobuf message
    request = class_pb2.Class(
        id=input("ID kelas yang ingin diubah: "),
        name=input("Nama kelas baru: "),
        location=input("Lokasi kelas baru: ")
    )

    # Memanggil method EditClass dari stub
    response = stub.EditClass(request)

    # Menampilkan data kelas yang telah diedit
    print(f'Kelas dengan ID {response.id} berhasil diedit\n')

# def EditClass():
#     print("=== Edit Kelas ===")
#     id = input("ID kelas yang akan diedit: ")
#     name = input("Nama kelas baru (kosongkan jika tidak ingin diubah): ")
#     location = input("Lokasi kelas baru (kosongkan jika tidak ingin diubah): ")

#     # membuat objek request
#     request = class_pb2.EditClassRequest(id=id, name=name, location=location)

#     # mengirim request ke server
#     response = stub.EditClass(request)

#     print(response.message)




# Fungsi untuk menghapus kelas
def RemoveClass():
    # Membuat instance RemoveClassRequest protobuf message
    request = class_pb2.Class(
        id=input("ID kelas yang akan dihapus: ")
    )

    # Memanggil method RemoveClass dari stub
    stub.RemoveClass(request)

    # Menampilkan pesan bahwa kelas telah dihapus
    print("Kelas berhasil dihapus\n")

# Menampilkan menu
while True:
    print("Menu:")
    print("1. Tampilkan semua kelas")
    print("2. Tambah kelas")
    print("3. Edit kelas")
    print("4. Hapus kelas")
    print("5. Keluar")

    choice = input("Pilih menu: ")

    if choice == '1':
        GetAllClasses()
    elif choice == '2':
        AddClass()
    elif choice == '3':
        EditClass()
    elif choice == '4':
        RemoveClass()
    elif choice == '5':
        break
    else:
        print("Menu tidak tersedia\n")

# Mengakhiri koneksi dengan server
channel.close()
