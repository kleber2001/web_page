import pymongo
import paramiko
import os

def back_up_ssh(ip_db,username_db):
    directories = ["/etc/shadow","/etc/passwd","/etc/group","/etc/gshadow"]
    directories1 = " ".join(directories)
    directories1 = directories1.strip()
    # Obtiene la ruta del escritorio del usuario actual
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    print(desktop_path)
    # Crea una nueva instancia de la clase SSHClient
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip_db, username=username_db, password='estudiante')
    sftp = ssh.open_sftp()
    ssh.exec_command('sudo su')
    ssh.exec_command('estudiante')
    ssh.exec_command('sudo tar -czf '+username_db+'.tar.gz '+directories1)
    sftp.get(username_db+'.tar.gz', os.path.join(desktop_path,username_db+'.tar.gz'))
    sftp.close()
    ssh.close()
    return None

PASSWORD= "9yrAHTDOLmFyaYmY"
MONGO_TIEMPO_FUERA= 1000
MONGO_BASEDATOS= "connection_ssh"
MONGO_COLECCION= "routes"
MONGO_URL="mongodb+srv://kgnunez:blbkD0pz8yPuA5mB@cluster0.kesacsi.mongodb.net/connection_ssh?retryWrites=true&w=majority"

try:
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]
    for datos in coleccion.find():
        user_name = datos["username"]
        user_ip = datos["ip"]
        back_up_ssh(user_ip,user_name)
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errortiempo:
    print("Tiempo excedido "+errortiempo)
except pymongo.errors.ConnectionFailure as errorconexion:
    print("Fallo al conectarse a Mongodb "+errorconexion)
