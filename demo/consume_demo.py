from kafkalibs.consumer import KafkaJSONConsumer

def handle_message(message):
    print("Processed:", message)

consumer = KafkaJSONConsumer("demo-topic", "demo-group")
consumer.consume(handle_message)
