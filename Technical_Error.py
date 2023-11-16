import pandas as pd
import os

video_names = ['A1', 'A2', 'A3', 'A4', 'A', 'B', 'C', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'U', 'V', 'W']

if __name__ == "__main__":
    directory_path = r'E:\Hassan Raza\Univeristy Of Essex\Dissertation\Code\Files\all files'
    df = None
    all_files_data = []
    i = 0
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_names = []
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)

        total_percentage = []
        new_header = df.iloc[29]
        df = df.iloc[30:]
        df.columns = new_header
        df.dropna(axis=1, how="all", inplace=True)

        print(filename)
        for video in video_names:
            file_names.append(filename.split(".")[0])

            data = df[df['SourceStimuliName'] == video][['Timestamp', 'Anger']]
            video_duration = (data['Timestamp'].max() - data['Timestamp'].min())/1000

            TimeStamp_each = []
            all_differences = []

            for index, row in data.iterrows():
                time, anger = row['Timestamp'], row['Anger']
                if pd.isna(anger):
                    TimeStamp_each.append(time)
                else:
                    TimeStamp_each.append(time)
                    difference_time = (TimeStamp_each[-1] - TimeStamp_each[0])/1000
                    all_differences.append(difference_time)
                    TimeStamp_each = [time]

            sumIsGreater = []
            for time in all_differences:
                if time >= 0.5:
                    sumIsGreater.append(time)

            percentage = (sum(sumIsGreater)/video_duration)*100
            total_percentage.append(percentage)

        average_data = {
                "participant": file_names,
                "video": video_names,
                "Percentage Failure": total_percentage,

            }
        all_files_data.append(average_data)

    data_frames = [pd.DataFrame(data) for data in all_files_data]

    combined_df = pd.concat(data_frames, ignore_index=True)

    path = rf'E:\Hassan Raza\Univeristy Of Essex\Dissertation\Code\Percentage Error File\PercentageError.csv'
    combined_df.to_csv(path, index=False)






