from datetime import timedelta


def study_time(filename: str):
    input_file = open(filename)
    days = []
    prev_finished = True
    prev_delta_1 = timedelta()

    for line in input_file.readlines():
        if len(line.strip()) == 3:
            days.append(timedelta())
        else:
            line_objects = line.strip().split('\t')
            time_string = line_objects[0]

            time_1 = time_string.split('-')[0]
            hours_1 = float(time_1.split(':')[0])
            minutes_1 = float(time_1.split(':')[1])
            delta_1 = timedelta(hours=hours_1,
                                minutes=minutes_1)

            if not prev_finished:
                days[-1] += delta_1 - prev_delta_1

            if '-' in time_string:  # введён диапазон
                time_2 = time_string.split('-')[1]
                hours_2 = float(time_2.split(':')[0])
                minutes_2 = float(time_2.split(':')[1])
                delta_2 = timedelta(hours=hours_2,
                                    minutes=minutes_2)
                prev_finished = True
                delta = delta_2 - delta_1
                days[-1] += delta
            else:
                prev_finished = False

            prev_delta_1 = delta_1

    return list(map(lambda dlt: str(dlt), days))


print(study_time('input_11-702.txt'))
