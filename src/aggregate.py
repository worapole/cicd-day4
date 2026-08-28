from pyspark.sql import functions as F

# ==========================================
# 1. Read source
# ==========================================
df_booking = spark.table(
    "samples.wanderbricks.bookings"
)

df_property = spark.table(
    "samples.wanderbricks.properties"
)

# ==========================================
# 2. Join
# ==========================================
df_join = (
    df_booking.alias("b")
    .join(
        df_property.alias("p"),
        F.col("b.property_id") == F.col("p.property_id"),
        "left"
    )
)

# ==========================================
# 3. Aggregate
# ==========================================
df_agg = (
    df_join
    .groupBy(
        F.to_date("b.created_at").alias("booking_date"),
        F.col("p.property_type").alias("property_type")
    )
    .agg(
        F.count("b.booking_id").alias("total_bookings"),
        F.sum("b.total_amount").alias("total_amount"),
        F.avg("b.total_amount").alias("avg_booking_amount"),
        F.sum("b.guests_count").alias("total_guests")
    )
)

# ==========================================
# 4. Preview
# ==========================================
display(
    df_agg.orderBy(
        "booking_date",
        "property_type"
    )
)

# ==========================================
# 5. Write Delta Table
# ==========================================
target_table = "ctl_training_dev.m7.booking_summary_chalanta"

(
    df_agg.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(target_table)
)

print(f"SUCCESS: {target_table} created")