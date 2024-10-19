import orb as orb
import sort as sort

def main():
    train_image_path = 'data/airPort.jpg'
    query_image_path = 'data/airportCrop.png'

    train_image_width, train_image_height, sorted_matches, \
    query_keypoints, train_keypoints = orb.orb_detect(train_image_path, query_image_path)

    sort.sort_keypoints_by_section(train_image_width, train_image_height, \
                                   sorted_matches, query_keypoints, \
                                   train_keypoints)


if __name__ == "__main__":
    main()
