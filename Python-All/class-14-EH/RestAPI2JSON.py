import requests
import json
import sys

def fetch_and_save_products():
    """
    Invoke REST API and write products data into a new JSON file
    """
    # Make the API request with timeout
    print("Fetching product data from API...")
    resp = requests.get('https://dummyjson.com/products', timeout=10)
    
    # Raise an exception for bad status codes (4xx, 5xx)
    resp.raise_for_status()
    
    # Parse JSON response
    product_data = resp.json()
    products = product_data.get('products', [])
    
    print(f"Successfully fetched {len(products)} products")
    
    # Write products to JSON file
    print("Writing data to product.json...")
    with open('product.json', 'w') as fp:
        json.dump(products, fp, indent=2)
    
    print("✅ New JSON File created successfully: product.json")
    print(f"   File contains {len(products)} products")

# Run the function
if __name__ == "__main__":
    fetch_and_save_products()