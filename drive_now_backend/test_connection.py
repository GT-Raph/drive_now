# test_connection.py
import socket
import psycopg2
from urllib.parse import urlparse

# Your connection string
DATABASE_URL = "postgresql://postgres:DWKThEpAfOOIbNhA@db.hupqccmpudnmfmgymohw.supabase.co:5432/postgres"

# Parse the URL
parsed = urlparse(DATABASE_URL)
hostname = parsed.hostname
port = parsed.port or 5432

print(f"Testing connection to: {hostname}:{port}")

# Test DNS resolution
try:
    ip_address = socket.gethostbyname(hostname)
    print(f"✓ DNS resolved: {hostname} → {ip_address}")
except socket.gaierror as e:
    print(f"✗ DNS failed: {e}")
    print("Try using Google DNS (8.8.8.8) or check your internet connection")
    exit(1)

# Test port connection
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip_address, port))
    if result == 0:
        print(f"✓ Port {port} is open on {ip_address}")
    else:
        print(f"✗ Port {port} is closed on {ip_address}")
    sock.close()
except Exception as e:
    print(f"✗ Connection test failed: {e}")

# Test database connection
print("\nTesting database connection...")
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✓ Database connection successful!")
    conn.close()
except Exception as e:
    print(f"✗ Database connection failed: {e}")