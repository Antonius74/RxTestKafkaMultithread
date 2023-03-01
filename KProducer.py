from kafka.producer import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(0, 1000000):
    s = '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' + str(i)


    future = producer.send('quickstart', bytes(s, 'utf-8'))
    #result = future.get(timeout=60)
    #print(result)