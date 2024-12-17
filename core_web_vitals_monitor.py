import time
import requests
import json
from tabulate import tabulate
from colorama import init, Fore

init()

def get_target_url():
    while True:
        url = raw_input("Input URL ~#: ").strip()
        if url:
            return url
        else:
            print(Fore.RED + "Error: URL cannot be empty. Please enter a valid URL.")

TARGET_URL = get_target_url()

def get_core_web_vitals(url):
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=desktop".format(url)
    response = requests.get(api_url)
    if response.status_code != 200:
        print(Fore.RED + "Error: Failed to retrieve data for {}".format(url))
        return None

    data = response.json()
    if "lighthouseResult" not in data:
        print(Fore.RED + "Error: Lighthouse result not found.")
        return None
    
    metrics = data["lighthouseResult"]["audits"]
    
    lcp = metrics["largest-contentful-paint"]["displayValue"]
    fid = metrics["interactive"]["displayValue"]
    cls = metrics["cumulative-layout-shift"]["displayValue"]

    return {"LCP": lcp, "FID": fid, "CLS": cls}

def print_report(data):
    headers = ["Metric", "Value"]
    table_data = [[metric, value] for metric, value in data.items()]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="center"))

def clean_value(value):
    return ''.join(filter(lambda x: x.isdigit() or x == '.', value))

def monitor_vitals():
    print(Fore.CYAN + "Core Web Vitals Monitor\n")
    print(Fore.GREEN + "Monitoring Core Web Vitals for: {}".format(TARGET_URL))

    while True:
        print(Fore.YELLOW + "\nFetching Core Web Vitals data...")
        vitals_data = get_core_web_vitals(TARGET_URL)
        
        if vitals_data:
            print_report(vitals_data)
            if "LCP" in vitals_data and "FID" in vitals_data and "CLS" in vitals_data:
                lcp_value = clean_value(vitals_data["LCP"])
                fid_value = clean_value(vitals_data["FID"])
                cls_value = clean_value(vitals_data["CLS"])

                if float(lcp_value) > 2.5:
                    print(Fore.RED + "Alert: LCP is too high! (Consider optimizing loading time)")
                if float(fid_value) > 100:
                    print(Fore.RED + "Alert: FID is too high! (Consider reducing input delay)")
                if float(cls_value) > 0.1:
                    print(Fore.RED + "Alert: CLS is too high! (Consider reducing layout shifts)")
        
        print(Fore.BLUE + "Waiting for the next check...")
        time.sleep(60)

if __name__ == "__main__":
    monitor_vitals()
