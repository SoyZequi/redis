import redis
import time

# Configuración de Redis
redis_host = 'redis-15797.c9.us-east-1-4.ec2.redns.redis-cloud.com'
redis_port = 15797
redis_password = '761313BzZJnGhDa3yFVPc1p5KRoMwh2c'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
