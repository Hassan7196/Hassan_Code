from emotion_vector_processor import output_vector_processor, video_emotion
from Final_Code_Pupil_Dilation import pupil_statistics_data
from gsr_feature_extraction import GSR_statisticsFeatures
from Heart_Rate_code import heartRate_statistics_data
from signalQualityGSR import GSRSignalQuality
import pandas as pd
import os
import statistics as stats
from scipy.stats import kurtosis
from Quality_Signals import quality_signals_FER, quality_signals_PupilSize, quality_signals_HeartRate


def statistics_features(data_path, processed_data_path):

    # GSR_quality_signals = GSRSignalQuality(GSR_QualitySignals)
    directory_path = data_path
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):

            file_path = os.path.join(directory_path, filename)
            file_names = []
            df = pd.read_csv(file_path)

            df.dropna(axis=1, how="all", inplace=True)


            # GSR features
            data_for_GSR = df[['Phasic Signal', 'Tonic Signal', 'Timestamp', 'SourceStimuliName']]
            GSR_data = GSR_statisticsFeatures(data_for_GSR)
            # print(GSR_data)

            # HeartRate Features
            data_for_heartRate = df[['Heart Rate PPG ALG', 'IBI PPG ALG', 'SourceStimuliName']]
            heartRate_data = heartRate_statistics_data(data_for_heartRate)

            # print(heartRate_data)
            # Pupil Features
            data_for_pupil = df[['ET_PupilLeft', 'ET_PupilRight', 'SourceStimuliName']]
            pupil_data = pupil_statistics_data(data_for_pupil)

            #Quality Signals
            data_for_qualitySignals_FER = df[['SourceStimuliName', 'Anger', 'Timestamp']]
            data_for_qualitySignals_PupilSize = df[['SourceStimuliName', 'ET_PupilLeft', 'Timestamp']]
            data_for_qualitySignals_HeartRate = df[['SourceStimuliName', 'IBI PPG ALG', 'Timestamp']]

            pupilSize_quality_signals = quality_signals_PupilSize(data_for_qualitySignals_PupilSize, filename)
            fer_quality_signals = quality_signals_FER(data_for_qualitySignals_FER, filename)
            heartRate_quality_signals = quality_signals_HeartRate(data_for_qualitySignals_HeartRate, filename)


           #
           # # arousal_valence_pairs = output_vector_processor(file_path)
           # #  all_values = arousal_valence_pairs
           #  emotions = list(video_emotion.keys())
           #  values = list(video_emotion.values())
           #  max_valence_values = []
           #  max_arousal_values = []
           #  min_valence_values = []
           #  min_arousal_values = []
           #  final_mean_arousal = []
           #  final_mean_valence = []
           #  std_deviation_arousal = []
           #  std_deviation_valence = []
           #  kurtosis_FER_arousal = []
           #  kurtosis_FER_valence = []
           #
           #  for emotion in emotions:
           #      sum_valence = 0
           #      sum_arousal = 0
           #      total_number_valence = 0
           #      total_number_arosual = 0
           #      file_names.append(filename.split(".")[0])
           #      current_emotion_data = all_values[emotion]
           #
           #      # Valence
           #      if len(current_emotion_data['valence']) > 0:
           #          max_min, max_max = min(current_emotion_data['valence']), max(current_emotion_data['valence'])
           #
           #          if max_max > abs(max_min):
           #              max_valence_values.append(max_max)
           #          else:
           #              max_valence_values.append(max_min)
           #
           #          if all(value > 0 for value in current_emotion_data['valence']):
           #              min_valence_values.append(min(current_emotion_data['valence']))
           #          elif all(value < 0 for value in current_emotion_data['valence']):
           #              min_valence_values.append(max(current_emotion_data['valence']))
           #          else:
           #              min_valence_values.append(0)
           #
           #          sum_valence += sum(current_emotion_data['valence'])
           #          total_number_valence += len(current_emotion_data['valence'])
           #
           #      else:
           #          max_valence_values.append(0)
           #          min_valence_values.append(0)
           #
           #      if len(current_emotion_data['valence']) > 1:
           #          std_deviation_valence.append(stats.stdev(current_emotion_data['valence']))
           #          kurtosis_FER_valence.append(kurtosis(current_emotion_data['valence']))
           #      else:
           #          std_deviation_valence.append(0)
           #          kurtosis_FER_valence.append(0)
           #
           #      # Arousal
           #      if len(current_emotion_data['arousal']) > 0:
           #          mini, maxi = min(current_emotion_data['arousal']), max(current_emotion_data['arousal'])
           #
           #          max_arousal_values.append(maxi)
           #          min_arousal_values.append(mini)
           #
           #          sum_arousal += sum(current_emotion_data['arousal'])
           #          total_number_arosual += len(current_emotion_data['arousal'])
           #      else:
           #          max_arousal_values.append(0)
           #          min_arousal_values.append(0)
           #
           #      if len(current_emotion_data['arousal']) > 1:
           #          std_deviation_arousal.append(stats.stdev(current_emotion_data['arousal']))
           #          kurtosis_FER_arousal.append(kurtosis(current_emotion_data['arousal']))
           #      else:
           #          std_deviation_arousal.append(0)
           #          kurtosis_FER_arousal.append(0)
           #
           #      final_mean_arousal.append(sum_arousal / total_number_arosual if total_number_arosual > 0 else 0)
           #      final_mean_valence.append(sum_valence / total_number_valence if total_number_valence > 0 else 0)

            features = {
                # "participant": file_names,
                # "video": values,
                # "FER_Mean_Valence": final_mean_valence,
                # "FER_Mean_Arousal": final_mean_arousal,
                # "FER_Std_Valence": std_deviation_valence,
                # "FER_Std_Arousal": std_deviation_arousal,
                # "FER_Kurtosis_Valence": kurtosis_FER_valence,
                # "FER_Kurtosis_Arousal": kurtosis_FER_arousal,
                # "FER_Max_Valence": max_valence_values,
                # "FER_Max_Arousal": max_arousal_values,
                # "FER_Min_Valence": min_valence_values,
                # "FER_Min_Arousal": min_arousal_values,
                "FER_Quality_Signals": fer_quality_signals['FER_Quality_Signals'],

                'Pupil_after_mean_normalize': pupil_data['after_mean_normalize'],
                'Pupil_after_min_normalize': pupil_data['after_min_normalize'],
                'Pupil_after_max_normalize': pupil_data['after_max_normalize'],
                'Pupil_after_skew_normalize': pupil_data['after_skew_normalize'],
                'Pupil_after_kurtosis_normalize': pupil_data['after_kurtosis_normalize'],
                'Pupil_after_std_normalize': pupil_data['after_std_normalize'],
                'Pupil_before_mean_normalize': pupil_data['before_mean_normalize'],
                'Pupil_before_min_normalize': pupil_data['before_min_normalize'],
                'Pupil_before_max_normalize': pupil_data['before_max_normalize'],
                'Pupil_before_skew_normalize': pupil_data['before_skew_normalize'],
                'Pupil_before_kurtosis_normalize': pupil_data['before_kurtosis_normalize'],
                'Pupil_before_std_normalize': pupil_data['before_std_normalize'],
                "Pupil_Quality_Signals": pupilSize_quality_signals['PupilSize_Quality_Signals'],

                'ibi_after_mean_normalize': heartRate_data['ibi_after_mean_normalize'],
                'ibi_after_min_normalize': heartRate_data['ibi_after_min_normalize'],
                'ibi_after_max_normalize': heartRate_data['ibi_after_max_normalize'],
                'ibi_after_skew_normalize': heartRate_data['ibi_after_skew_normalize'],
                'ibi_after_kurtosis_normalize': heartRate_data['ibi_after_kurtosis_normalize'],
                'ibi_after_std_normalize': heartRate_data['ibi_after_std_normalize'],
                'ibi_before_mean_normalize': heartRate_data['ibi_before_mean_normalize'],
                'ibi_before_min_normalize': heartRate_data['ibi_before_min_normalize'],
                'ibi_before_max_normalize': heartRate_data['ibi_before_max_normalize'],
                'ibi_before_skew_normalize': heartRate_data['ibi_before_skew_normalize'],
                'ibi_before_kurtosis_normalize': heartRate_data['ibi_before_kurtosis_normalize'],
                'ibi_before_std_normalize': heartRate_data['ibi_before_std_normalize'],
                'heart_rate_after_mean_normalize': heartRate_data['heart_rate_after_mean_normalize'],
                'heart_rate_after_min_normalize': heartRate_data['heart_rate_after_min_normalize'],
                'heart_rate_after_max_normalize': heartRate_data['heart_rate_after_max_normalize'],
                'heart_rate_after_skew_normalize': heartRate_data['heart_rate_after_skew_normalize'],
                'heart_rate_after_kurtosis_normalize': heartRate_data['heart_rate_after_kurtosis_normalize'],
                'heart_rate_after_std_normalize': heartRate_data['heart_rate_after_std_normalize'],
                'heart_rate_before_mean_normalize': heartRate_data['heart_rate_before_mean_normalize'],
                'heart_rate_before_min_normalize': heartRate_data['heart_rate_before_min_normalize'],
                'heart_rate_before_max_normalize': heartRate_data['heart_rate_before_max_normalize'],
                'heart_rate_before_skew_normalize': heartRate_data['heart_rate_before_skew_normalize'],
                'heart_rate_before_kurtosis_normalize': heartRate_data['heart_rate_before_kurtosis_normalize'],
                'heart_rate_before_std_normalize': heartRate_data['heart_rate_before_std_normalize'],
                'ibi_after_rmssd_normalize': heartRate_data['ibi_after_rmssd_normalize'],
                'ibi_after_sdnn_normalize': heartRate_data['ibi_after_sdnn_normalize'],
                'ibi_before_rmssd_normalize': heartRate_data['ibi_before_rmssd_normalize'],
                'ibi_before_sdnn_normalize': heartRate_data['ibi_before_sdnn_normalize'],
                "HeartRate_Quality_Signals": heartRate_quality_signals ['HeartRate_Quality_Signals'],

                'phasic_signal_after_mean_normalize': GSR_data['phasic_signal_after_mean_normalize'],
                'phasic_signal_after_median_normalize': GSR_data['phasic_signal_after_median_normalize'],
                'phasic_signal_after_min_normalize': GSR_data['phasic_signal_after_min_normalize'],
                'phasic_signal_after_max_normalize': GSR_data['phasic_signal_after_max_normalize'],
                'phasic_signal_after_skew_normalize': GSR_data['phasic_signal_after_skew_normalize'],
                'phasic_signal_after_kurtosis_normalize': GSR_data['phasic_signal_after_kurtosis_normalize'],
                'phasic_signal_after_std_normalize': GSR_data['phasic_signal_after_std_normalize'],
                'phasic_signal_after_variance_normalize': GSR_data['phasic_signal_after_variance_normalize'],
                'phasic_signal_after_mean_energy_normalize': GSR_data['phasic_signal_after_mean_energy_normalize'],
                'phasic_signal_after_peak_average_normalize': GSR_data['phasic_signal_after_peak_average_normalize'],
                'phasic_signal_after_peak_per_minute_normalize': GSR_data['phasic_signal_after_peak_per_minute_normalize'],

                'phasic_signal_before_mean_normalize': GSR_data['phasic_signal_before_mean_normalize'],
                'phasic_signal_before_median_normalize': GSR_data['phasic_signal_before_median_normalize'],
                'phasic_signal_before_min_normalize': GSR_data['phasic_signal_before_min_normalize'],
                'phasic_signal_before_max_normalize': GSR_data['phasic_signal_before_max_normalize'],
                'phasic_signal_before_skew_normalize': GSR_data['phasic_signal_before_skew_normalize'],
                'phasic_signal_before_kurtosis_normalize': GSR_data['phasic_signal_before_kurtosis_normalize'],
                'phasic_signal_before_std_normalize': GSR_data['phasic_signal_before_std_normalize'],
                'phasic_signal_before_variance_normalize': GSR_data['phasic_signal_before_variance_normalize'],
                'phasic_signal_before_mean_energy_normalize': GSR_data['phasic_signal_before_mean_energy_normalize'],
                'phasic_signal_before_peak_average_normalize': GSR_data['phasic_signal_before_peak_average_normalize'],
                'phasic_signal_before_peak_per_min_normalize': GSR_data['phasic_signal_before_peak_per_min_normalize'],

                'tonic_signal_after_mean_normalize': GSR_data['tonic_signal_after_mean_normalize'],
                'tonic_signal_after_median_normalize': GSR_data['tonic_signal_after_median_normalize'],
                'tonic_signal_after_min_normalize': GSR_data['tonic_signal_after_min_normalize'],
                'tonic_signal_after_max_normalize': GSR_data['tonic_signal_after_max_normalize'],
                'tonic_signal_after_skew_normalize': GSR_data['tonic_signal_after_skew_normalize'],
                'tonic_signal_after_kurtosis_normalize': GSR_data['tonic_signal_after_kurtosis_normalize'],
                'tonic_signal_after_std_normalize': GSR_data['tonic_signal_after_std_normalize'],
                'tonic_signal_after_variance_normalize': GSR_data['tonic_signal_after_variance_normalize'],
                'tonic_signal_after_mean_energy_normalize': GSR_data['tonic_signal_after_mean_energy_normalize'],

                'tonic_signal_before_mean_normalize': GSR_data['tonic_signal_before_mean_normalize'],
                'tonic_signal_before_median_normalize': GSR_data['tonic_signal_before_median_normalize'],
                'tonic_signal_before_min_normalize': GSR_data['tonic_signal_before_min_normalize'],
                'tonic_signal_before_max_normalize': GSR_data['tonic_signal_before_max_normalize'],
                'tonic_signal_before_skew_normalize': GSR_data['tonic_signal_before_skew_normalize'],
                'tonic_signal_before_kurtosis_normalize': GSR_data['tonic_signal_before_kurtosis_normalize'],
                'tonic_signal_before_std_normalize': GSR_data['tonic_signal_before_std_normalize'],
                'tonic_signal_before_variance_normalize': GSR_data['tonic_signal_before_variance_normalize'],
                'tonic_signal_before_mean_energy_normalize': GSR_data['tonic_signal_before_mean_energy_normalize'],
            }

        df = pd.DataFrame(features)
        path = processed_data_path + rf'\{filename}'
        print(path)
        df.to_csv(path, index=False)
