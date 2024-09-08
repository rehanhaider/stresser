from src import load_test, analyze_results
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stress Testing Tool")
    parser.add_argument("--url", type=str, default="http://your-apache-server.com/your-php-script.php", help="URL of the server")
    parser.add_argument("--requests", type=int, default=1000, help="Number of requests")
    parser.add_argument("--users", type=int, default=50, help="Number of concurrent users")
    args = parser.parse_args()

    print(f"Starting load test with {args.requests} requests and {args.users} concurrent users...")
    results = load_test(args.url, args.requests, args.users)
    print("Load test completed. Analyzing results...")
    analyze_results(results)
    
