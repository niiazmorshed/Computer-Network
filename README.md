# CSE421 — Computer Networks

Coursework for CSE421 (Computer Networks): a network design project, hands-on labs and lecture material.

---

## ⭐ Featured Project — [Smart Healthcare Network Design](Smart-Healthcare-Network/)

A 6-site healthcare network built in Cisco Packet Tracer. It uses VLSM addressing, RIPv2 with static-route redistribution, next-hop/exit-interface/recursive/floating static routes, automatic failover, DHCP, and DNS/Web/Email services.

**→ [View the project](Smart-Healthcare-Network/)**

---

## Labs

| Lab | Topic | Tools |
|-----|-------|-------|
| [Lab 1 — Basic Router Config](Labs/Lab1-Basic-Router-Config/) | Hostnames, passwords, banners, interface addressing | Packet Tracer, Cisco IOS |
| [Lab 2 — Wireshark: HTTP & SMTP](Labs/Lab2-Wireshark-HTTP-SMTP/) | Packet capture and protocol analysis, UDP echo simulation | Wireshark, ns-3 (Python) |
| [Lab 3 — Socket Programming](Labs/Lab3-Socket-Programming/) | TCP client/server apps, including a multi-threaded server | Python `socket`, `threading` |
| [Lab 4 — DHCP, Static Routing & RIPv2](Labs/Lab4-DHCP-Static-Routing-RIPv2/) | DHCPv4 (IOS and server), static/default/floating routes, RIPv2 | Packet Tracer, Cisco IOS |

### Running Lab 3

```bash
cd Labs/Lab3-Socket-Programming/Task1
python task1_server.py   # terminal 1
python task1_client.py   # terminal 2
```

| Task | What it does |
|------|--------------|
| 1 | The client sends its hostname, and the server logs the client's IP and hostname |
| 2 | The server counts the vowels in a message and replies |
| 3 | The same as Task 2, with a multi-threaded server for clients connecting at the same time |
| 4 | The server works out a salary from hours worked (with overtime) and checks the input |

---

## Theory

[`Theory/`](Theory/): lecture slides (protocols, application/transport/network/data-link layers, IPv6) and assignments.
