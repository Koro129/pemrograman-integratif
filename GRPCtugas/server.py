from concurrent import futures
import grpc
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import class_pb2
import class_pb2_grpc

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate('<PATH-UNTUK-FILE-serviceAccountKey.json>')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Kelas service
class ClassService(class_pb2_grpc.ClassServiceServicer):
    def GetAllClasses(self, request, context):
        classes = []
        # Mengambil semua dokumen dari koleksi "classes" di Firebase
        for doc in db.collection("classes").stream():
            data = doc.to_dict()
            # Membuat instance protobuf message dari data dokumen
            class_ = class_pb2.Class(
                id=doc.id,
                name=data['name'],
                location=data['location']
            )
            classes.append(class_)
        # Membuat instance protobuf message response dengan semua data produk
        response = class_pb2.AllClasses(classes=classes)
        return response

    def AddClass(self, request, context):
        # Menambahkan data kelas baru ke koleksi "classes" di Firebase
        doc_ref = db.collection('classes').document(request.id)
        doc_ref.set({
            'name': request.name,
            'location': request.location
        })
        # Membuat instance protobuf message response dengan ID kelas yang ditambahkan
        response = class_pb2.ClassID(id=request.id)
        return response

    def EditClass(self, request, context):
        # Memperbarui data kelas dengan ID yang diberikan di koleksi "classes" di Firebase
        doc_ref = db.collection('classes').document(request.id)
        doc_ref.update({
            'name': request.name,
            'location': request.location
        })
        # Membuat instance protobuf message response dengan ID kelas yang diperbarui
        response = class_pb2.ClassID(id=request.id)
        return response

    def RemoveClass(self, request, context):
        # Menghapus data kelas dengan ID yang diberikan dari koleksi "classes" di Firebase
        db.collection('classes').document(request.id).delete()
        # Tidak perlu membuat protobuf message response karena tidak ada data yang dikembalikan
        return class_pb2.Empty()

# Main program
if __name__ == '__main__':
    # Menjalankan gRPC server pada port 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    class_pb2_grpc.add_ClassServiceServicer_to_server(ClassService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051")
    server.wait_for_termination()
