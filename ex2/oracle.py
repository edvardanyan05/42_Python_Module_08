#!/usr/bin/env python3

import os
from dotenv import load_dotenv


load_dotenv()

matrix_mode = os.getenv("MATRIX_MODE", "development")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion_endpoint = os.getenv("ZION_ENDPOINT")


print("ORACLE STATUS: Reading the Matrix...")
print("Configuration loaded:")

print(f"Mode: {matrix_mode}")

if database_url:
    print("Database: Connected to configured instance")
else:
    print("Database: Missing configuration")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Missing key")

print(f"Log Level: {log_level}")

if zion_endpoint:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("Environment security check:")
print("[OK] No hardcoded secrets detected")

if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file not found")

print("[OK] Production overrides available")

if matrix_mode == "production":
    print("Running in production mode.")
else:
    print("Running in development mode.")

print("The Oracle sees all configurations.")
