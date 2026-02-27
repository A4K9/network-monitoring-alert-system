# Network Monitoring & Alert System

A Python-based monitoring system designed to track network endpoint availability and performance.

## Features
- Detects server availability (UP / DOWN)
- Identifies performance degradation (SLOW)
- Logs incidents automatically
- Sends real-time email alerts

## How It Works
The system continuously checks network endpoints by establishing connections and measuring response time (latency).  
If a service becomes unavailable or exceeds the latency threshold, it logs the issue and sends an alert.

## Tech Used
- Python
- Socket Programming
- Email SMTP Alerts

## How to Run

1. Add endpoints in targets.txt
2. Configure email settings in monitor.py
3. Run:

python monitor.py

## Purpose
Built to simulate real-world NOC monitoring workflows such as availability tracking, incident logging, and alerting.
