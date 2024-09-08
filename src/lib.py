import requests
import time
import concurrent.futures
from statistics import mean

def make_request(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response_time = time.time() - start_time
        return response.status_code, response_time
    except requests.RequestException as e:
        return str(e), time.time() - start_time

def load_test(url, num_requests, concurrent_users):
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_users) as executor:
        future_to_url = {executor.submit(make_request, url): url for _ in range(num_requests)}
        for future in concurrent.futures.as_completed(future_to_url):
            results.append(future.result())
    
    return results

def analyze_results(results):
    successful_requests = [r for r in results if isinstance(r[0], int) and 200 <= r[0] < 300]
    failed_requests = [r for r in results if r not in successful_requests]
    
    response_times = [r[1] for r in successful_requests]
    
    print(f"Total requests: {len(results)}")
    print(f"Successful requests: {len(successful_requests)}")
    print(f"Failed requests: {len(failed_requests)}")
    print(f"Average response time: {mean(response_times):.2f} seconds")
    print(f"Minimum response time: {min(response_times):.2f} seconds")
    print(f"Maximum response time: {max(response_times):.2f} seconds")

