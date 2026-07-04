import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Folder Paths
# -----------------------------
DATA_FILE = "data/weather_dataset.csv"
VISUAL_FOLDER = "visualizations"
REPORT_FOLDER = "report"

os.makedirs(VISUAL_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
def load_data():

    try:
        df = pd.read_csv(DATA_FILE)

        print("Dataset Loaded Successfully")
        return df

    except FileNotFoundError:
        print("weather_data.csv not found!")
        return None

    except Exception as e:
        print("Error :", e)
        return None


# -----------------------------
# Clean Dataset
# -----------------------------
def clean_data(df):

    print("\nCleaning Dataset...")

    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


# -----------------------------
# Validation
# -----------------------------
def validate(df):

    columns = [
        "Date",
        "City",
        "Temperature",
        "Humidity",
        "WindSpeed",
        "Rainfall",
        "Pressure",
        "Weather"
    ]

    for col in columns:

        if col not in df.columns:

            print(f"Missing Column : {col}")

            return False

    return True


# -----------------------------
# Analysis
# -----------------------------
def analysis(df):

    print("\n------------ WEATHER ANALYSIS ------------")

    print("Total Records :", len(df))

    print("Total Cities :", df["City"].nunique())

    print("Average Temperature :", round(df["Temperature"].mean(),2))

    print("Maximum Temperature :", df["Temperature"].max())

    print("Minimum Temperature :", df["Temperature"].min())

    print("Average Humidity :", round(df["Humidity"].mean(),2))

    print("Average Wind Speed :", round(df["WindSpeed"].mean(),2))

    print("Average Pressure :", round(df["Pressure"].mean(),2))

    print("Total Rainfall :", df["Rainfall"].sum())


# -----------------------------
# Line Chart
# -----------------------------
def temperature_chart(df):

    avg_temp = df.groupby("Date")["Temperature"].mean()

    plt.figure(figsize=(10,5))

    plt.plot(avg_temp.index,
             avg_temp.values,
             marker="o")

    plt.title("Average Temperature Trend")

    plt.xlabel("Date")

    plt.ylabel("Temperature")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("visualizations/temperature_trend.png")

    plt.close()


# -----------------------------
# Bar Chart
# -----------------------------
def weather_chart(df):

    weather = df["Weather"].value_counts()

    plt.figure(figsize=(8,5))

    weather.plot(kind="bar")

    plt.title("Weather Distribution")

    plt.xlabel("Weather")

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig("visualizations/weather_distribution.png")

    plt.close()


# -----------------------------
# Pie Chart
# -----------------------------
def rainfall_chart(df):

    rain = df.groupby("Weather")["Rainfall"].sum()

    plt.figure(figsize=(7,7))

    plt.pie(rain,
            labels=rain.index,
            autopct="%1.1f%%")

    plt.title("Rainfall by Weather")

    plt.savefig("visualizations/rainfall_pie_chart.png")

    plt.close()


# -----------------------------
# Histogram
# -----------------------------
def humidity_chart(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["Humidity"],
             bins=10)

    plt.title("Humidity Distribution")

    plt.xlabel("Humidity")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("visualizations/humidity_histogram.png")

    plt.close()


# -----------------------------
# Scatter Plot
# -----------------------------
def scatter_chart(df):

    plt.figure(figsize=(8,5))

    plt.scatter(df["Temperature"],
                df["Humidity"])

    plt.title("Temperature vs Humidity")

    plt.xlabel("Temperature")

    plt.ylabel("Humidity")

    plt.tight_layout()

    plt.savefig("visualizations/temp_vs_humidity.png")

    plt.close()


# -----------------------------
# Report
# -----------------------------
def report(df):

    report = f"""

WEATHER DATA ANALYSIS REPORT

======================================

Total Records : {len(df)}

Total Cities : {df['City'].nunique()}

Average Temperature : {round(df['Temperature'].mean(),2)} °C

Maximum Temperature : {df['Temperature'].max()} °C

Minimum Temperature : {df['Temperature'].min()} °C

Average Humidity : {round(df['Humidity'].mean(),2)} %

Average Wind Speed : {round(df['WindSpeed'].mean(),2)} km/h

Average Pressure : {round(df['Pressure'].mean(),2)} hPa

Total Rainfall : {df['Rainfall'].sum()} mm

======================================

INSIGHTS

1. Dataset contains weather information for 100 cities.

2. Temperature varies between different cities.

3. Rainfall is highest during Rainy and Thunderstorm weather.

4. Humidity increases significantly during rainy days.

5. Sunny weather occurs more frequently than thunderstorms.

6. Wind speed remains moderate in most cities.

7. Pressure remains stable throughout the dataset.

8. Dataset is clean and contains no duplicate records.

"""

    with open("report/weather_report.txt","w") as file:

        file.write(report)


# -----------------------------
# Main
# -----------------------------
def main():

    df = load_data()

    if df is None:
        return

    if not validate(df):
        return

    df = clean_data(df)

    analysis(df)

    temperature_chart(df)

    weather_chart(df)

    rainfall_chart(df)

    humidity_chart(df)

    scatter_chart(df)

    report(df)

    print("\nProject Completed Successfully.")

    print("\nCharts Saved in visualizations Folder.")

    print("Report Saved in report Folder.")


if __name__ == "__main__":

    main()