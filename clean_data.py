import pandas as pd

# 1. 加载 CSV
df = pd.read_csv("data/realtor-data.csv")

# 2. 清理空值和无效数据
df = df.dropna(subset=["price", "bed", "bath", "city", "state", "zip_code"])
df = df[df["price"] > 1000]  # 排除明显错误的价格

# 3. 创建描述字段（用于向量化）
def create_description(row):
    return (
        f" A {row['bed']}-bed, {row['bath']}-bath home "
        f"of {row['house_size']} sqft in {row['city']}, {row['state']} "
        f"({row['zip_code']}), listed at ${row['price']}. "
        f"Land size is {row['acre_lot']} acres. Status: {row['status']}."
    )

df["description"] = df.apply(create_description, axis=1)

# 4. 截取一部分用于测试（例如每州最多 100 条）
sampled = df.groupby("state").apply(lambda x: x.sample(min(100, len(x)))).reset_index(drop=True)

# 5. 保存清洗后的数据
sampled.to_csv("cleaned_real_estate_data.csv", index=False)