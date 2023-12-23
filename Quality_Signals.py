import pandas as pd
import os

video_names = ['A1', 'A2', 'A3', 'A4', 'A', 'B', 'C', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'U', 'V', 'W']


def quality_signals_FER(df, filename):
    total_percentage = []
    file_names = []

    # print(filename)
    for video in video_names:
        file_names.append(filename.split(".")[0])

        data = df[df['SourceStimuliName'] == video][['Timestamp', 'Anger']]
        video_duration = (data['Timestamp'].max() - data['Timestamp'].min()) / 1000

        TimeStamp_each = []
        all_differences = []

        for index, row in data.iterrows():
            time, anger = row['Timestamp'], row['Anger']
            if pd.isna(anger):
                TimeStamp_each.append(time)
            else:
                TimeStamp_each.append(time)
                difference_time = (TimeStamp_each[-1] - TimeStamp_each[0]) / 1000
                all_differences.append(difference_time)
                TimeStamp_each = [time]

        sumIsGreater = []
        for time in all_differences:
            if time >= 0.5:
                sumIsGreater.append(time)

        percentage = (sum(sumIsGreater) / video_duration) * 100
        total_percentage.append(percentage)

    Quality_Signal_data = {
        "participant": file_names,
        "video": video_names,
        "FER_Quality_Signals": total_percentage,

    }
    return Quality_Signal_data


def quality_signals_PupilSize(df, filename):
    total_percentage = []
    file_names = []

    # print(filename)
    for video in video_names:
        file_names.append(filename.split(".")[0])

        data = df[df['SourceStimuliName'] == video][['Timestamp', 'ET_PupilLeft']]
        video_duration = (data['Timestamp'].max() - data['Timestamp'].min()) / 1000

        TimeStamp_each = []
        all_differences = []

        for index, row in data.iterrows():
            time, pupil = row['Timestamp'], row['ET_PupilLeft']
            if pupil == "-1":
                TimeStamp_each.append(time)
            else:
                TimeStamp_each.append(time)
                difference_time = (TimeStamp_each[-1] - TimeStamp_each[0]) / 1000
                all_differences.append(difference_time)
                TimeStamp_each = [time]

        sumIsGreater = []
        for time in all_differences:
            if time >= 0.5:
                sumIsGreater.append(time)

        percentage = (sum(sumIsGreater) / video_duration) * 100
        total_percentage.append(percentage)

    Quality_Signal_data = {
        "participant": file_names,
        "video": video_names,
        "PupilSize_Quality_Signals": total_percentage,

    }
    return Quality_Signal_data


def quality_signals_HeartRate(df, filename):
    total_percentage = []
    file_names = []

    # print(filename)
    for video in video_names:
        file_names.append(filename.split(".")[0])

        data = df[df['SourceStimuliName'] == video][['Timestamp', 'IBI PPG ALG']]
        video_duration = (data['Timestamp'].max() - data['Timestamp'].min()) / 1000

        TimeStamp_each = []
        all_differences = []

        for index, row in data.iterrows():
            time, pupil = row['Timestamp'], row['IBI PPG ALG']
            if pupil == "-1":
                TimeStamp_each.append(time)
            else:
                TimeStamp_each.append(time)
                difference_time = (TimeStamp_each[-1] - TimeStamp_each[0]) / 1000
                all_differences.append(difference_time)
                TimeStamp_each = [time]

        sumIsGreater = []
        for time in all_differences:
            if time >= 0.5:
                sumIsGreater.append(time)

        percentage = (sum(sumIsGreater) / video_duration) * 100
        total_percentage.append(percentage)

    Quality_Signal_data = {
        "participant": file_names,
        "video": video_names,
        "HeartRate_Quality_Signals": total_percentage,

    }
    return Quality_Signal_data

def quality_signals_GSR(df, filename):
    total_percentage = []
    file_names = []

    # print(filename)
    for video in video_names:
        file_names.append(filename.split(".")[0])

        data = df[df['SourceStimuliName'] == video][['Timestamp', 'Phasic Signal']]
        video_duration = (data['Timestamp'].max() - data['Timestamp'].min()) / 1000

        TimeStamp_each = []
        all_differences = []

        for index, row in data.iterrows():
            time, phasic = row['Timestamp'], row['Phasic Signal']
            if pd.isna(phasic):
                TimeStamp_each.append(time)
            else:
                TimeStamp_each.append(time)
                difference_time = (TimeStamp_each[-1] - TimeStamp_each[0]) / 1000
                all_differences.append(difference_time)
                TimeStamp_each = [time]

        sumIsGreater = []
        for time in all_differences:
            if time >= 0.5:
                sumIsGreater.append(time)

        percentage = (sum(sumIsGreater) / video_duration) * 100
        total_percentage.append(percentage)

    Quality_Signal_data = {
        "participant": file_names,
        "video": video_names,
        "GSR_Quality_Signals": total_percentage,

    }
    return Quality_Signal_data
