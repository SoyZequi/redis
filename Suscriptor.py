import redis

# Configuración de Redis
redis_host = 'redis-15797.c9.us-east-1-4.ec2.redns.redis-cloud.com'
redis_port = 15797
redis_password = '761313BzZJnGhDa3yFVPc1p5KRoMwh2c'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
