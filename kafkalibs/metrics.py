from prometheus_client import Counter, start_http_server

# Start the Prometheus metrics server on port 8001
start_http_server(8001)

# Producer metrics
producer_success_counter = Counter('kafka_producer_success_total', 'Number of successfully produced Kafka messages')
producer_failure_counter = Counter('kafka_producer_failure_total', 'Number of failed Kafka message sends')

# Consumer metrics
consumer_success_counter = Counter('kafka_consumer_success_total', 'Number of successfully processed Kafka messages')
consumer_failure_counter = Counter('kafka_consumer_failure_total', 'Number of failed Kafka message processings')
