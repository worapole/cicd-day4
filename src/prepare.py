from pyspark.sql import functions as F

# ==========================================
# Source Tables
# ==========================================
source_tables = [
    "samples.wanderbricks.bookings",
    "samples.wanderbricks.properties"
]

# ==========================================
# 1. Display all source tables
# ==========================================
print("===== SOURCE TABLES =====")

for table_name in source_tables:
    df = spark.table(table_name)
    row_count = df.count()

    print(f"Table     : {table_name}")
    print(f"Row Count : {row_count}")
    print("-" * 50)

    if row_count == 0:
        raise Exception(
            f"FAILED: {table_name} has no data"
        )

# ==========================================
# 2. Check booking date
# ==========================================
df_booking = spark.table(
    "samples.wanderbricks.bookings"
)

df_date = (
    df_booking
    .select(
        F.to_date("created_at").alias("booking_date")
    )
    .distinct()
    .orderBy("booking_date")
)

print("===== AVAILABLE BOOKING DATES =====")

display(df_date)

if df_date.count() == 0:
    raise Exception(
        "FAILED: No booking date found"
    )

# ==========================================
# SUCCESS
# ==========================================
print("SUCCESS: All source tables are ready")