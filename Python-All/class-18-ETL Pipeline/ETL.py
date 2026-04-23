# Extract - Transform - Load (ETL) Example
import requests
import csv
import mysql.connector
import json
import pymongo


API_URL = "https://dummyjson.com/products"


# -------------------- Extract --------------------
def extract_data():
    try:
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        return resp.json()['products']
    except requests.exceptions.RequestException as err:
        print("API Error:", err)
        return []


# -------------------- Transform --------------------
def transform_data(products):
    beauty_products_csv = []
    beauty_products_json = []

    for product in products:
        if product['category'] == "beauty":

            beauty_products_csv.append((
                product['id'],
                product['title'],
                product['price'],
                product['category'],
                product['rating']
            ))

            beauty_products_json.append({
                "pid": product['id'],
                "pname": product['title'],
                "price": product['price'],
                "category": product['category'],
                "rating": product['rating']
            })

    return beauty_products_csv, beauty_products_json


# -------------------- Load CSV --------------------
def load_csv(data):
    try:
        with open('products.csv', 'w', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerow(['pid', 'pname', 'price', 'category', 'rating'])
            writer.writerows(data)

        print("CSV file created successfully")

    except IOError as err:
        print("CSV File Error:", err)


# -------------------- Load MySQL --------------------
def load_mysql(data):

    try:
        dbcon = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='6pm'
        )

        cursor = dbcon.cursor()

        sql = """
        INSERT INTO products(pid,pname,price,category,rating)
        VALUES(%s,%s,%s,%s,%s)
        """

        cursor.executemany(sql, data)
        dbcon.commit()

        print("Inserted into MySQL:", cursor.rowcount)

    except mysql.connector.Error as err:
        print("MySQL Error:", err)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'dbcon' in locals() and dbcon.is_connected():
            dbcon.close()


# -------------------- Load JSON --------------------
def load_json(data):
    try:
        with open('products.json', 'w') as fp:
            json.dump(data, fp, indent=4)

        print("JSON file created successfully")

    except IOError as err:
        print("JSON File Error:", err)


# -------------------- Load MongoDB --------------------
def load_mongodb(data):

    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['6pm']
        product_col = db['products']

        product_col.insert_many(data)

        print("Inserted into MongoDB successfully")

    except Exception as err:
        print("MongoDB Error:", err)


# -------------------- Main ETL Process --------------------
def main():

    products = extract_data()

    if not products:
        print("No data received from API")
        return

    csv_data, json_data = transform_data(products)

    load_csv(csv_data)
    load_mysql(csv_data)
    load_json(json_data)
    load_mongodb(json_data)


if __name__ == "__main__":
    main()