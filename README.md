# 🔒 Network Intrusion Detection System (NIDS) with Zeek, Suricata & ELK

## 📖 About the Project

This project is a Network Intrusion Detection System (NIDS) built using Suricata, Zeek, and the ELK Stack (Elasticsearch, Logstash, Kibana) to detect, analyze, and visualize malicious network activity in real time.
	•	Suricata provides signature-based detection of threats such as exploits, scans, and malware.
	•	Zeek offers behavior-based analysis and protocol-level metadata.
	•	Logstash processes and parses logs before indexing them into Elasticsearch.
	•	Elasticsearch stores events for fast searching and querying.
	•	Kibana provides dashboards for monitoring alerts and traffic patterns.

The repository includes configuration files, an Elasticsearch index template, and a traffic generation script for replaying PCAPs or simulating activity. This framework is designed for researchers, students, and security engineers to experiment with intrusion detection, perform threat hunting, and monitor live or captured traffic.

⸻

## ⚙️ Requirements
	•	Ubuntu 20.04 (recommended)
	•	Zeek
	•	Suricata
	•	Elasticsearch
	•	Logstash
	•	Kibana

⸻

## 🚀 Installation

Clone the repository:

git clone https://github.com/yourusername/nids-zeek-suricata.git
cd nids-zeek-suricata


Install dependencies:

sudo apt update
sudo apt install -y zeek suricata elasticsearch logstash kibana

-----

## 🛠️ Configuration

The repo includes sample configs you can customize:
	•	suricata.yaml – Suricata IDS/IPS configuration
	•	local.zeek & zeekctl.cfg – Zeek protocol and logging configs
	•	logstash.conf – Logstash pipeline for parsing and sending data to Elasticsearch
	•	template.json – Elasticsearch index template for storing alerts
	•	generate_traffic.sh – Script to simulate or replay PCAP traffic

## ▶️ How to Use
	1.	Start Suricata
 sudo suricata -c suricata.yaml -i <interface>

 	2.	Start Zeek
  zeek -i <interface>

  3.	Load Logstash Pipeline
  sudo logstash -f logstash.conf

  4.	Import Elasticsearch Template
  curl -X PUT "localhost:9200/_template/nids" -H 'Content-Type: application/json' -d @template.json

 	5.	Run Kibana and access the web interface at:
  http://localhost:5601

  6.	Generate Traffic for Testing
  bash generate_traffic.sh

## 📊 Visualization

Once Kibana is running, create an index pattern (nids-*) and explore:
	•	Real-time alerts from Suricata and Zeek
	•	Protocol metadata and flow data
	•	Dashboards for network activity and intrusion attempts
