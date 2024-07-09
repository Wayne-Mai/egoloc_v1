import json
import numpy as np

def merge_json_files(json1_path, json2_path, output_path):
    # Load the JSON files
    with open(json1_path, 'r') as file:
        data1 = json.load(file)
    
    with open(json2_path, 'r') as file:
        data2 = json.load(file)
    
    count=0
    # Merge the data
    for video_uid in data2:
        if video_uid in data1:
            good_poses1 = data1[video_uid]['good_poses']
            camera_poses1 = data1[video_uid]['camera_poses']
            good_poses2 = data2[video_uid]['good_poses']
            camera_poses2 = data2[video_uid]['camera_poses']
            
            for i, good_pose in enumerate(good_poses2):
                if good_pose and not good_poses1[i]:
                    good_poses1[i] = True
                    camera_poses1[i] = camera_poses2[i]
                    
                    count+=1
                    print(f"{count} : Updated {video_uid} {i} ")
                    
        # else:
        #     data1[video_uid] = data2[video_uid]

    # Save the merged data to a new JSON file
    with open(output_path, 'w') as file:
        json.dump(data1, file, indent=4)