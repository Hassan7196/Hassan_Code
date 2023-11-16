from emotion_vector_processor import output_vector_processor, video_emotion
import pandas as pd
import os
import statistics as stats
from scipy.stats import kurtosis


def statistics_features(data_path, processed_data_path):

    average_data = {}

    directory_path = data_path
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            file_names = []
            arousal_valence_pairs = output_vector_processor(file_path)
            all_values = arousal_valence_pairs
            emotions = list(video_emotion.keys())
            values = list(video_emotion.values())
            max_valence_values = []
            max_arousal_values = []
            min_valence_values = []
            min_arousal_values = []
            final_mean_arousal = []
            final_mean_valence = []
            std_deviation_arousal = []
            std_deviation_valence = []
            kurtosis_FER_arousal = []
            kurtosis_FER_valence = []

            for emotion in emotions:
                sum_valence = 0
                sum_arousal = 0
                total_number_valence = 0
                total_number_arosual = 0
                file_names.append(filename.split(".")[0])
                current_emotion_data = all_values[emotion]

                if len(current_emotion_data['valence']) > 0:
                    max_valence_values.append(max(current_emotion_data['valence']))
                    min_valence_values.append(min(current_emotion_data['valence']))

                    sum_valence += sum(current_emotion_data['valence'])
                    total_number_valence += len(current_emotion_data['valence'])

                else:
                    max_valence_values.append(0)
                    min_valence_values.append(0)

                if len(current_emotion_data['valence']) > 1:
                    std_deviation_valence.append(stats.stdev(current_emotion_data['valence']))
                    kurtosis_FER_valence.append(kurtosis(current_emotion_data['valence']))
                else:
                    std_deviation_valence.append(0)
                    kurtosis_FER_valence.append(0)

                if len(current_emotion_data['arousal']) > 0:
                    max_arousal_values.append(max(current_emotion_data['arousal']))
                    min_arousal_values.append(min(current_emotion_data['arousal']))
                    sum_arousal += sum(current_emotion_data['arousal'])
                    total_number_arosual += len(current_emotion_data['arousal'])
                else:
                    max_arousal_values.append(0)
                    min_arousal_values.append(0)

                if len(current_emotion_data['arousal']) > 1:
                    std_deviation_arousal.append(stats.stdev(current_emotion_data['arousal']))
                    kurtosis_FER_arousal.append(kurtosis(current_emotion_data['arousal']))
                else:
                    std_deviation_arousal.append(0)
                    kurtosis_FER_arousal.append(0)

                final_mean_arousal.append(sum_arousal / total_number_arosual if total_number_arosual > 0 else 0)
                final_mean_valence.append(sum_valence / total_number_valence if total_number_valence > 0 else 0)

            average_data = {
                "participant": file_names,
                "video": values,
                "Mean_FER_Valence": final_mean_valence,
                "Mean_FER_Arousal": final_mean_arousal,
                "Std_FER_Valence": std_deviation_valence,
                "Std_FER_Arousal": std_deviation_arousal,
                "Kurtosis_FER_Valence": kurtosis_FER_valence,
                "Kurtosis_FER_Arousal": kurtosis_FER_arousal,
                "Max_FER_Valence": max_valence_values,
                "Max_FER_Arousal": max_arousal_values,
                "Min_FER_Valence": min_valence_values,
                "Min_FER_Arousal": min_arousal_values,
            }
            print(average_data)
        df = pd.DataFrame(average_data)
        path = processed_data_path+rf'\{filename}'
        print(path)
        df.to_csv(path, index=False)
