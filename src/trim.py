
# Expects a list of sections, each with keypoints
# Returns a list of sections, each with keypoints, with an 18 keypoint sum between the lists 
#   (assuming there are at least that many to begin with -- there may be less, there may not be more)
# In a perfect dataset, each list is trimmed to two keypoints. In an imperfect dataset, certain lists 
#   will make up for lacking lists by including more than two keypoints, to maintain a sum of 18.
#   ... An even more imperfect dataset contains a sum of less than 18 keypoints.   

def trim_sections(sections_list):
    sect1 = sect2 = sect3 = sect4 = sect5 \
    = sect6 = sect7 = sect8 = sect9 = []

    trimmed_sections_list = [sect1, sect2, sect3, sect4, sect5, sect6, sect7, sect8, sect9]
    
    keypoint_count = 0

    while (keypoint_count < 18):
        for i, section in enumerate(sections_list):
            if (len(section) != 0):
                trimmed_sections_list[i].append(section.pop(0))
                keypoint_count += 1
    

    #transform list to two-dimensions:
    flattened_trimmed_sections_list = [item if isinstance(item, list) else [item] for sublist in trimmed_sections_list for item in (sublist if isinstance(sublist, list) else [sublist])]
    
    # Uncomment to print unflattened trimmed_sections_list:
    # print('\nTRIMMED: \n')
    # for i, each in enumerate(trimmed_sections_list):
    #     print(f'Section {i}: {trimmed_sections_list[i]} \n\n')

    # trimmed_sections_list is being returned to visualize each list in main (can eventually be removed after visualization is not necessary)
    # flattemed_trimmed_sections_list of being returned to be used as ground control porints for georeference() call in main
    return trimmed_sections_list, flattened_trimmed_sections_list

