import pandas as pd
import glob
import os

def main():
    print("Starting Cyclistic Data Processing...")
    
    # Define paths (assuming script is run from the Scripts folder)
    # Use absolute paths or reliable relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_path = os.path.join(script_dir, "..", "Data", "raw_data")
    processed_data_path = os.path.join(script_dir, "..", "Data", "processed_data")
    
    # Ensure processed directory exists
    os.makedirs(processed_data_path, exist_ok=True)
    
    # 1. Data Aggregation
    print("1. Reading and concatenating CSV files...")
    csv_files = glob.glob(os.path.join(raw_data_path, "*.csv"))
    if not csv_files:
        print("No CSV files found in the raw_data directory.")
        return
        
    df_list = []
    for f in csv_files:
        print(f"   Reading {os.path.basename(f)}...")
        df_list.append(pd.read_csv(f))
        
    df = pd.concat(df_list, ignore_index=True)
    print(f"Total rows loaded: {len(df):,}")

    # 2. Data Reduction
    print("2. Dropping irrelevant columns...")
    columns_to_drop = ['start_lat', 'start_lng', 'end_lat', 'end_lng']
    # Drop only if they exist in the dataframe
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # 3. Handling Missing Values
    print("3. Dropping rows with missing station names...")
    df = df.dropna(subset=['start_station_name', 'end_station_name'])
    print(f"Rows remaining after dropping missing stations: {len(df):,}")

    # 4. Data Transformation
    print("4. Transforming data (datetimes, calculating ride length, extracting dates)...")
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    
    # Calculate ride length in minutes
    df['ride_length_mins'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60.0
    
    # Extract day of week and month
    df['day_of_week'] = df['started_at'].dt.day_name()
    df['month'] = df['started_at'].dt.month_name()

    # 5. Data Filtering
    print("5. Filtering out bad data (duration <= 0 or > 24 hours)...")
    df = df[(df['ride_length_mins'] > 0) & (df['ride_length_mins'] <= 1440)]
    print(f"Rows remaining after time filters: {len(df):,}")

    # 6. Aggregation for Tableau
    print("6. Creating lightweight summary datasets for visualization...")
    
    # Summary 1: Usage by user type and day of week
    summary_day = df.groupby(['member_casual', 'day_of_week']).agg(
        total_rides=('ride_length_mins', 'count'),
        avg_ride_length=('ride_length_mins', 'mean')
    ).reset_index()
    
    # Sort days of week
    day_cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    summary_day['day_of_week'] = pd.Categorical(summary_day['day_of_week'], categories=day_cats, ordered=True)
    summary_day = summary_day.sort_values(['member_casual', 'day_of_week'])
    
    # Summary 2: Usage by user type and month
    summary_month = df.groupby(['member_casual', 'month']).agg(
        total_rides=('ride_length_mins', 'count'),
        avg_ride_length=('ride_length_mins', 'mean')
    ).reset_index()
    
    # Sort months (Based on the 12 months provided starting Sept)
    month_cats = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    summary_month['month'] = pd.Categorical(summary_month['month'], categories=month_cats, ordered=True)
    summary_month = summary_month.sort_values(['member_casual', 'month'])

    # Save the summaries
    day_path = os.path.join(processed_data_path, "summary_by_day.csv")
    month_path = os.path.join(processed_data_path, "summary_by_month.csv")
    
    summary_day.to_csv(day_path, index=False)
    summary_month.to_csv(month_path, index=False)
    
    print("Data processing complete!")
    print(f" - {day_path}")
    print(f" - {month_path}")

if __name__ == "__main__":
    main()
