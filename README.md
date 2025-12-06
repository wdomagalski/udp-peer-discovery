# udp-peer-discovery
Python experiment with LAN peer discovery using UDP broadcast.
One script listens for discovery packets and replies, the other broadcasts a message and waits for responses.

## How to run

Terminal 1:

```bash
python3 peer_listener.py
```

Terminal 2:

```bash
python3 discover_broadcast.py
```

## Notes
- Works only on local networks – broadcast is not routed.
- It is a very simple experiment to demonstrate how basic peer discovery works.
