from datetime import datetime, timedelta

time_format = "%H:%M"


def account_for_stop(time_list, time_after_stop, time_before_stop):
    updated_times = []
    for time_str in time_list:
        time_obj = datetime.strptime(time_str, time_format)
        if time_before_stop > 0:
            for i in range(time_before_stop):
                updated_time_obj = time_obj - timedelta(minutes=i)
                updated_time_str = updated_time_obj.strftime(time_format)
                updated_times.append(updated_time_str)
        if time_after_stop > 0:
            for i in range(time_after_stop):
                updated_time_obj = time_obj + timedelta(minutes=i)
                updated_time_str = updated_time_obj.strftime(time_format)
                updated_times.append(updated_time_str)

    return updated_times


def available_times(station):
    available = []
    for hour in range(0, 24):
        for minute in range(0, 60):
            if hour < 10 and minute < 10:
                time_str = f"0{hour}:0{minute}"
                if time_str not in station:
                    available.append(time_str)
            elif hour < 10 <= minute:
                time_str = f"0{hour}:{minute}"
                if time_str not in station:
                    available.append(time_str)
            elif hour >= 10 > minute:
                time_str = f"{hour}:0{minute}"
                if time_str not in station:
                    available.append(time_str)
            else:
                time_str = f"{hour}:{minute}"
                if time_str not in station:
                    available.append(time_str)

    return available


def find_trip(stations, current_station, start_time, travel_time, wait_time, trip):
    start_time_obj = datetime.strptime(start_time, time_format)
    calculated_time_str = (start_time_obj + timedelta(minutes=travel_time)).strftime(time_format)
    time_before_stop = 2
    time_after_stop = 6
    station_keys = list(stations.keys())
    current_station_index = station_keys.index(current_station)
    if current_station_index + 1 < len(station_keys):
        next_station = station_keys[current_station_index + 1]
    else:
        return trip
    if calculated_time_str not in available_times(
            account_for_stop(stations[next_station], time_after_stop, time_before_stop)):
        if wait_time < 5:
            diff_start_time = (datetime.strptime(start_time, "%H:%M") + timedelta(minutes=1)).strftime("%H:%M")
            wait_time += 1
            return find_trip(stations, current_station, diff_start_time, travel_time, wait_time, trip)
        else:
            diff_start_time = (datetime.strptime(start_time, "%H:%M") + timedelta(minutes=travel_time)).strftime("%H:%M")
            return find_trip(stations, next_station, diff_start_time, travel_time, wait_time, trip)

    if wait_time >= 5:
        wait_time = 0
        return find_trip(stations, next_station, calculated_time_str, travel_time, wait_time, trip)
    else:
        wait_time = 0
        trip.append(current_station)
        return find_trip(stations, next_station, calculated_time_str, travel_time, wait_time, trip)


stacje = {
    "stacja_1": ["12:10", "12:40", "13:00", "13:20", "14:00", "14:20", "15:00", "15:30", "16:00", "16:20", "17:44",
                 "18:00", "18:40", "19:00", "20:12", "22:00", "23:00", "23:59"],
    "stacja_2": ["11:30", "12:00", "12:30", "13:15", "13:45", "14:30", "15:15", "15:45", "16:30", "17:00", "17:30",
                 "18:15", "18:45", "19:30", "20:00", "21:00", "22:30", "23:45"],
    "stacja_3": ["10:45", "11:15", "11:45", "12:30", "13:00", "13:45", "14:15", "15:00", "15:30", "16:15", "16:45",
                 "17:30", "18:00", "18:45", "19:15", "20:00", "21:15", "22:45"],
    "stacja_4": ["09:15", "09:45", "10:30", "11:00", "11:45", "12:15", "13:00", "13:30", "14:15", "14:45", "15:30",
                 "16:00", "16:45", "17:15", "18:00", "19:30", "20:45", "22:00"],
    "stacja_5": ["08:30", "09:00", "09:30", "10:15", "10:45", "11:30", "12:15", "12:45", "13:30", "14:00", "14:30",
                 "15:15", "15:45", "16:30", "17:00", "18:00", "19:15", "20:30"],
    "stacja_6": ["07:45", "08:15", "08:45", "09:30", "10:00", "10:45", "11:15", "12:00", "12:30", "13:15", "13:45",
                 "14:30", "15:00", "15:45", "16:15", "17:00", "18:15", "19:30"],
    "stacja_7": ["06:50", "07:20", "07:50", "08:35", "09:05", "09:50", "10:20", "11:05", "11:35", "12:20", "12:50",
                 "13:35", "14:05", "14:50", "15:20", "16:20", "17:35", "18:50"],
    "stacja_8": ["06:05", "06:35", "07:05", "07:50", "08:20", "09:05", "09:35", "10:20", "10:50", "11:35", "12:05",
                 "12:50", "13:20", "14:05", "14:35", "15:35", "16:50", "18:05"],
    "stacja_9": ["05:20", "05:50", "06:20", "07:05", "07:35", "08:20", "08:50", "09:35", "10:05", "10:50", "11:20",
                 "12:05", "12:35", "13:20", "13:50", "14:50", "16:05", "17:20"],
    "stacja_10": ["04:35", "05:05", "05:35", "06:20", "06:50", "07:35", "08:05", "08:50", "09:20", "10:05", "10:35",
                  "11:20", "11:50", "12:35", "13:05", "14:05", "15:20", "16:35"],
}

trasa = find_trip(stacje, "stacja_1", "11:00", 15, 0, trip=[])

for t in trasa:
    print(t, end=" ")
