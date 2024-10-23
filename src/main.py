import orb as orb
import sort as sort
import folder_prompt as folder_prompt

def main():
    train_image_path = 'data/airPort.jpg'
    query_image_path = 'data/airportCrop.png'

    train_image_width, train_image_height, sorted_matches, \
    query_keypoints, train_keypoints = orb.orb_detect(train_image_path, query_image_path)

    sort.sort_keypoints_by_section(train_image_width, train_image_height, \
                                   sorted_matches, query_keypoints, \
                                   train_keypoints)

    # print(folder_prompt.get_input_path())
    # print(folder_prompt.get_output_path())

if __name__ == "__main__":
    main()
