from Statistics_Features import statistics_features
from Combining_all_Statistics_Features import combining_statistics_features
from merge_files import merge_file

if __name__ == "__main__":

    repository_data = {}
    with open("repository.txt", "r") as txt_file:
        for line in txt_file:
            name, url = line.strip().split(',')
            repository_data[name] = url

    # Access repositories using the dictionary
    repository_name_1 = "data_files"
    data_files_path = repository_data[repository_name_1]

    repository_name_2 = "Features_files"
    features_files_path = repository_data[repository_name_2]

    repository_name_3 = "Combined_File"
    combined_file_path = repository_data[repository_name_3]

    repository_name_4 = "Ground_truth_File"
    Ground_truth_File = repository_data[repository_name_4]

    repository_name_5 = "merge_File"
    merge_File = repository_data[repository_name_5]

    while True:
        print("\nChoose a function:")
        print("1. Convert Imotion Data files into statistics Features files")
        print("2. Combined all features data files")
        print("3. Merge all data with Ground Truth")

        choice = input("Enter the number of the function you want to choose: ")

        if choice == "1":
            print("\nNow go to the Respository.txt file, Change the Paths of Line 1, where you have all the data files,"
                  " and Line 2, where u want all of you files after processed, ")
            choice_2 = input("\nPress 1 to continue, or any other number to go back to previous statement:")
            if choice_2 == "1":
                statistics_features(data_files_path, features_files_path)
            else:
                continue
        if choice == "2":
            print("\n Now go to the Respository.txt file, Change the Path of Line 2, where you have all the "
                  "statistics features data files, "
                  " \nfrom Choice 1, And Line 3 path to where you want to add your combined feature file")
            choice_2 = input("\nPress 1 to continue, or any other number to go back to previous statement:")
            if choice_2 == "1":
                combining_statistics_features(features_files_path, combined_file_path)
            else:
                continue

        if choice == "3":
            print("\n Now go to the Respository.txt file, Change the Path of Line 3, where you have combined features "
                  "file from Choice 2, \n "
                  "Line 4 path where you have ground truth file"
                  "\n and line 5 where want your merge file to be")
            choice_2 = input("\nPress 1 to continue, or any other number to go back to previous statement:")
            if choice_2 == "1":
                merge_file(combined_file_path, Ground_truth_File, merge_File)
            else:
                continue

