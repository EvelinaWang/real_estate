import os
import openai
import pandas as pd
import singlestoredb as s2
from dotenv import load_dotenv
from tqdm import tqdm

tqdm.pandas()
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# 加载你刚刚清洗的数据
df = pd.read_csv("data/snippet.csv")

# Step 1: 为每个 description 生成 embedding
def get_embedding(text, model="text-embedding-ada-002"):

    response = openai.Embedding.create(input=[text], model=model)

    return response["data"][0]["embedding"]

df["embedding"] = df["description"].progress_apply(get_embedding)

# Step 2: 连接 SingleStore 数据库        
conn = s2.connect(
    os.environ["SINGLESTORE_URI"]
)

print("连接成功？", conn.open)

cursor = conn.cursor()

# Step 3: 创建表（向量+元数据）
cursor.execute("""
CREATE TABLE IF NOT EXISTS real_estate_embeddings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    price DOUBLE,
    bed INT,
    bath INT,
    embedding BLOB
);
""")

# Step 4: 插入数据（embedding 需转换为 bytes）
import struct

def vector_to_bytes(vector):
    return struct.pack('%sf' % len(vector), *vector)

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO real_estate_embeddings 
        (description, city, state, zip_code, price, bed, bath, embedding)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["description"],
        row["city"],
        row["state"],
        row["zip_code"],
        row["price"],
        row["bed"],
        row["bath"],
        vector_to_bytes(row["embedding"])
    ))

conn.commit()
conn.close()
