# Core Web Vitals Monitor

This tool is designed to monitor Core Web Vitals of a URL in real-time. Using data from the **Google PageSpeed Insights API** (Lighthouse), it tracks key metrics: **Largest Contentful Paint (LCP)**, **First Input Delay (FID)**, and **Cumulative Layout Shift (CLS)**.

## Features

- **Real-time monitoring** of Core Web Vitals such as LCP, FID, and CLS for a website.
- **Alerts** when the LCP, FID, or CLS values exceed thresholds that may negatively impact user experience.
- **Displays data in a table format** for better readability using the `tabulate` library.
- **Automatic cleaning** of values by removing units like "s" from LCP and FID to allow proper processing.

## Requirements

- Python 2.7 (Python 3.x is recommended)
- Python libraries:
  - `requests` - to make HTTP requests to the Google PageSpeed Insights API.
  - `tabulate` - to display results in a table format.
  - `colorama` - to colorize the terminal output.

## Installation

1. **Install dependencies**:
   Before using this tool, make sure to install the required libraries. Run the following command in your terminal:

   ```bash
   pip install requests tabulate colorama
   ```

2. **Running the Tool**:
   Once dependencies are installed, you can run the tool with the following command:

   ```bash
   python core_web_vitals_monitor.py
   ```

   The tool will prompt you to enter the URL you want to monitor.

## Usage

1. **Enter URL**: After running the tool, you will be prompted to enter the URL of the website you want to monitor.
2. **Real-Time Monitoring**: The tool will monitor Core Web Vitals every 60 seconds and display metrics like LCP, FID, and CLS in a clear table format.
3. **Alerts**: If any metric exceeds the set threshold (LCP > 2.5 seconds, FID > 100ms, CLS > 0.1), the tool will display an alert in the terminal.

### Example Output:

```
Core Web Vitals Monitor

Monitoring Core Web Vitals for: https://example.com

Fetching Core Web Vitals data...

╒══════════╤═════════╕
│  Metric  │  Value  │
╞══════════╪═════════╡
│   FID    │  1.5 s  │
├──────────┼─────────┤
│   LCP    │  1.4 s  │
├──────────┼─────────┤
│   CLS    │  0.003  │
╘══════════╧═════════╛

Waiting for the next check...
```

If LCP, FID, or CLS exceed the threshold, you will see alerts like:

```
Alert: LCP is too high! (Consider optimizing loading time)
Alert: FID is too high! (Consider reducing input delay)
Alert: CLS is too high! (Consider reducing layout shifts)
```
## Threshold Customization

- **LCP**: If greater than 2.5 seconds, considered too slow.
- **FID**: If greater than 100ms, considered too high.
- **CLS**: If greater than 0.1, considered too high.

You can customize these threshold values in the code inside the `monitor_vitals()` function if necessary.