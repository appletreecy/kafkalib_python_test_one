# 🐍 Kafka Python App with Prometheus Metrics (Pre-Docker)

This is a Python-based Kafka producer/consumer library with built-in Prometheus metrics for tracking message success and failure counts. This version runs **outside of Docker**, using a local Python environment and local Kafka setup.

---

## 📁 Project Structure

```
kafkalibs_test_one/
├── kafkalibs/
│   ├── __init__.py
│   ├── producer.py
│   ├── consumer.py
│   ├── config.py              # Kafka config (edit broker here)
│   └── metrics.py             # Prometheus metrics exposed at :8001
├── demo/
│   ├── produce_demo.py        # Example: sends messages to Kafka
│   └── consume_demo.py        # Example: consumes and processes Kafka messages
├── requirements.txt
└── README.md
```

---

## 🧪 Step-by-Step Usage

### 1. 🔧 Setup Python Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist yet:
```txt
kafka-python
prometheus_client
loguru
```

---

### 2. 🧱 Start Kafka and Zookeeper Locally

Make sure you have Kafka and Zookeeper running.  
Example using Docker:

```bash
docker network create kafka-net

docker run -d --name zookeeper --network kafka-net -p 2181:2181 \
  zookeeper

docker run -d --name kafka --network kafka-net -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  wurstmeister/kafka
```

---

### 3. 📤 Run Kafka Producer

In one terminal:

```bash
python demo/produce_demo.py
```

This sends a few example JSON messages to Kafka topic `demo-topic`.

---

### 4. 📥 Run Kafka Consumer

In another terminal:

```bash
python demo/consume_demo.py
```

This consumes messages from `demo-topic` and processes them.

---

### 5. 📈 Expose Prometheus Metrics

Once either demo script is running, Prometheus metrics are exposed at:

```
http://localhost:8001/metrics
```

You’ll see counters like:

- `kafka_producer_success_total`
- `kafka_producer_failure_total`
- `kafka_consumer_success_total`
- `kafka_consumer_failure_total`

---

## ⚙️ Change Kafka Broker or Topic

Edit the values in `kafkalibs/config.py`:

```python
KAFKA_BROKER_URL = "localhost:9092"
DEFAULT_TOPIC = "demo-topic"
```

---

## 💡 Tips

- Make sure topic `demo-topic` exists (or allow auto-create in Kafka).
- To switch between producer and consumer, change the script run.
- Prometheus will scrape `localhost:8001` if you configure it.
- This version runs manually without Docker. To containerize, see the Docker README instead.

---

## ✅ Next Steps

- [ ] Add Prometheus and Grafana integration (see Docker version)
- [ ] Containerize for production use
- [ ] Add Avro or schema registry support (optional)

---

## 📜 License

MIT License
