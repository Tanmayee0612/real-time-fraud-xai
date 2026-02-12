import pandas as pd
import requests
import time
import json

# =====================================
# Configuration
# =====================================

DATA_PATH = "transactions.csv"
MODEL_API_URL = "http://localhost:8000/predict"

print("\n=== Real-Time Transaction Simulation System ===")
STREAM_DELAY = float(input("Enter stream delay in seconds (e.g., 1 or 0.5): "))


# =====================================
# Load Transactions
# =====================================

def load_transactions(path):
    try:
        df = pd.read_csv(path)
        print(f"\nLoaded {len(df)} transactions successfully.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


# =====================================
# Send Transaction to Model API
# =====================================

def send_to_model(transaction):
    try:
        response = requests.post(
            MODEL_API_URL,
            json=transaction,
            timeout=3
        )
        return response.json(), False
    except Exception as e:
        return {"error": "Model not reachable"}, True


# =====================================
# Real-Time Streaming Simulation
# =====================================

def simulate_stream(df):
    print("\nStarting Real-Time Transaction Stream...\n")

    latencies = []
    results = []
    failure_count = 0

    start_total_time = time.time()

    for index, row in df.iterrows():
        transaction = row.to_dict()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        start_time = time.time()
        prediction, failed = send_to_model(transaction)
        end_time = time.time()

        latency = (end_time - start_time) * 1000
        latencies.append(latency)

        if failed:
            failure_count += 1

        results.append({
            "transaction_id": index + 1,
            "timestamp": timestamp,
            "prediction": prediction,
            "latency_ms": latency
        })

        print(f"Transaction ID: {index + 1}")
        print(f"Timestamp: {timestamp}")
        print(f"Prediction: {prediction}")
        print(f"Latency: {latency:.3f} ms")
        print("-" * 50)

        time.sleep(STREAM_DELAY)

    end_total_time = time.time()

    # =====================================
    # Performance Metrics
    # =====================================

    total_time = end_total_time - start_total_time
    avg_latency = sum(latencies) / len(latencies)
    max_latency = max(latencies)
    throughput = len(df) / total_time
    failure_rate = (failure_count / len(df)) * 100

    print("\n========== SYSTEM PERFORMANCE ==========")
    print(f"Transactions Processed: {len(df)}")
    print(f"Average Latency: {avg_latency:.3f} ms")
    print(f"Max Latency: {max_latency:.3f} ms")
    print(f"Throughput: {throughput:.2f} tx/sec")
    print(f"API Failure Rate: {failure_rate:.2f}%")

    if failure_rate > 20:
        print("System Status: DEGRADED (Model API Issues Detected)")
    else:
        print("System Status: STABLE")

    # Save Performance Metrics
    performance_data = {
        "transactions_processed": len(df),
        "average_latency_ms": avg_latency,
        "max_latency_ms": max_latency,
        "throughput_tx_per_sec": throughput,
        "failure_rate_percent": failure_rate
    }

    with open("performance_metrics.json", "w") as f:
        json.dump(performance_data, f, indent=4)

    # Save Detailed Transaction Log
    with open("transaction_log.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\nDetailed logs saved to transaction_log.json")
    print("Performance metrics saved to performance_metrics.json")


# =====================================
# Main
# =====================================

if __name__ == "__main__":
    df = load_transactions(DATA_PATH)
    if df is not None:
        simulate_stream(df)
