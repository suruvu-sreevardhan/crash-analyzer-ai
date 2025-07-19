from datetime import datetime, timedelta

def parse_logs_near_timestamp(file_path, crash_time_str):
    with open(file_path, "r") as f:
        logs = f.readlines()

    crash_time = datetime.fromisoformat(crash_time_str)
    window = timedelta(minutes=10)
    extracted_logs = []

    for line in logs:
        try:
            ts_part = line.split(" ")[0]
            ts = datetime.fromisoformat(ts_part)
            if crash_time - window <= ts <= crash_time + window:
                extracted_logs.append(line)
        except:
            continue

    return "\n".join(extracted_logs)
