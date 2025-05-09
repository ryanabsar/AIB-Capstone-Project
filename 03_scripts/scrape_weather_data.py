import requests
import demjson3
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from fake_useragent import UserAgent
import time
import random
from tqdm import tqdm
import html
import pandas as pd

# Extract Weather Info from JSON entry
def extract_weather_info(data_entry, date_str):
    result = []

    for item in data_entry.get('c', []):
        h_val = item.get('h', '')
        soup = BeautifulSoup(h_val, 'html.parser')

        if '<br>' in h_val:
            try:
                parts = h_val.split('<br>')
                time_part = BeautifulSoup(parts[0], 'html.parser').text.strip()
                # print(time_part)
                full_datetime_str = f"{date_str} {time_part}"
                dt = datetime.strptime(full_datetime_str, "%Y%m%d %H:%M")
                result.append(dt)
            except Exception:
                result.append(None)

        elif soup.img and soup.img.get('title'):
            result.append(soup.img['title'])

        elif soup.span and soup.span.get('title'):
            result.append(soup.span['title'])

        elif 'mph' in h_val:
            try:
                mph = float(''.join(c for c in h_val if c.isdigit() or c == '.'))
                mps = round(mph * 0.44704, 2)
                result.append(mps)
            except ValueError:
                result.append(None)

        elif any(unit in h_val for unit in ['°F', '&nbsp;', 'Hg', 'mi']):
            try:
                text = html.unescape(soup.text)
                if text == "N/A":
                    result.append(None)
                else:
                    digits = ''.join(c for c in text if c.isdigit() or c == '.')
                    result.append(float(digits) if '.' in digits else int(digits))
            except ValueError:
                result.append(None)

        elif '%' in h_val:
            try:
                percent_val = int(h_val.replace('%', '').strip())
                result.append(percent_val)
            except ValueError:
                result.append(None)

        else:
            text = soup.text.strip()
            if text.upper() == "N/A":
                result.append(None)
            elif ':' in text or ('am' in text.lower() or 'pm' in text.lower()):
                full_datetime_str = f"{date_str} {text}"
                # print(full_datetime_str)
                dt = datetime.strptime(full_datetime_str, "%Y%m%d %H:%M")
                # print(dt)
                result.append(dt)
            else:
                result.append(soup.text.strip())

    return result

# Fetch weather data for a specific date
def fetch_weather_for_date(date, user_agent):
    headers = {"User-Agent": user_agent}
    date_str = date.strftime('%Y%m%d')

    query_params = {
        "n": "uk/kirkwall",
        "mode": "historic",
        "hd": date_str,
        "month": date.month,
        "year": date.year,
        "json": "1"
    }

    url = "https://www.timeanddate.com/scripts/cityajax.php"
    response = requests.get(url, headers=headers, params=query_params)
    
    #save response to file
    

    if response.status_code != 200:
        print(f"Failed to fetch data for {date_str}")
        return []
    # else:
    #     # print(f"Successfully fetched data for {date_str}")
    #     with open(f"./04_outputs/03_jsons/response_{date_str}.json", "w") as f:
    #         f.write(response.text)

    try:
        raw_data = demjson3.decode(response.text)
        if not isinstance(raw_data, list):
            print(f"Unexpected data format for {date_str}")
            return []
    except Exception as e:
        print(f"Error decoding data for {date_str}: {e}")
        return []

    records = []
    for entry in raw_data:
        try:
            text = extract_weather_info(entry, date_str=date_str)
            records.append(text)
        except Exception as e:
            print(f"Error parsing entry for {date_str}: {e}")

    return records

def weather_scraper(start_str='2017-01-01', end_str='2017-01-01', csv_path=None):
    start_date = datetime.strptime(start_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_str, "%Y-%m-%d")
    total_days = (end_date - start_date).days + 1

    ua = UserAgent()
    all_records = []
    current_date = start_date

    for _ in tqdm(range(total_days), desc="Fetching weather data"):
        day_records = fetch_weather_for_date(current_date, ua.random)
        all_records.extend(day_records)
        current_date += timedelta(days=1)
        time.sleep(random.uniform(1, 3))

    columns = [
        "Time", "Icon", "Temperature (F)", "Description", "Wind Speed (m/s)",
        "Wind Direction", "Humidity (%)", "Pressure (Hg)", "Visibility (mi)"
    ]

    df_ws = pd.DataFrame(all_records, columns=columns)
    print(df_ws.Time[0])
    df_ws["Time"] = pd.to_datetime(df_ws["Time"], errors="coerce",format="%Y-%m-%d %H:%M:%S")

    print(df_ws.head())
    
    if csv_path:
        df_ws.to_csv(csv_path, index=False)
        print(f"Data saved to {csv_path}")

    return df_ws

if __name__ == "__main__":
    # Example usage
    # weather_scraper(start_str='2017-01-01', end_str='2017-01-31')
    start_str = '2017-01-01'
    end_str = '2017-01-01'
    data = weather_scraper(start_str=start_str,end_str=end_str)
    print(data.shape)
