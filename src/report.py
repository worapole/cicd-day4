from pathlib import Path
import matplotlib.pyplot as plt
from pyspark.sql import functions as F


def write_report(df, out_dir) -> "list[Path]":
    """
    Generate booking summary artifacts.

    Artifacts:
      1. booking_by_property_type.png
      2. summary.md

    Returns:
        List of artifact paths written.
    """

    # ==========================================
    # 1. Prepare output directory
    # ==========================================
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    written = []

    # ==========================================
    # 2. Aggregate bookings by property type
    # ==========================================
    df_chart = (
        df
        .groupBy("property_type")
        .agg(
            F.sum("total_bookings").alias("total_bookings"),
            F.sum("total_amount").alias("total_amount"),
            F.sum("total_guests").alias("total_guests")
        )
        .orderBy(F.desc("total_bookings"))
    )

    pdf = df_chart.toPandas()

    # ==========================================
    # 3. Create chart
    # ==========================================
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(
        pdf["property_type"],
        pdf["total_bookings"]
    )

    ax.set_title("Total Bookings by Property Type")
    ax.set_xlabel("Property Type")
    ax.set_ylabel("Total Bookings")

    plt.xticks(rotation=45)
    plt.tight_layout()

    # ==========================================
    # 4. Save chart
    # ==========================================
    chart_path = out / "booking_by_property_type.png"

    fig.savefig(
        chart_path,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(fig)

    written.append(chart_path)

    # ==========================================
    # 5. Create summary.md
    # ==========================================
    summary_path = out / "summary.md"

    total_bookings = pdf["total_bookings"].sum()
    total_amount = pdf["total_amount"].sum()
    total_guests = pdf["total_guests"].sum()

    lines = [
        "# Booking Summary Report",
        "",
        f"Total bookings: {total_bookings:,.0f}",
        f"Total amount: {total_amount:,.2f}",
        f"Total guests: {total_guests:,.0f}",
        "",
        "## Booking by Property Type",
        "",
        "| Property Type | Total Bookings | Total Amount | Total Guests |",
        "|---|---:|---:|---:|"
    ]

    for _, row in pdf.iterrows():
        lines.append(
            f"| {row['property_type']} "
            f"| {row['total_bookings']:,.0f} "
            f"| {row['total_amount']:,.2f} "
            f"| {row['total_guests']:,.0f} |"
        )

    summary_path.write_text(
        "\n".join(lines) + "\n"
    )

    written.append(summary_path)

    return written

#####################################################

table_name = "ctl_training_dev.m7.booking_summary_chalanta"

df = spark.table(table_name)

written = write_report(
    df,
    "/tmp/booking_report"
)

for path in written:
    print(path)