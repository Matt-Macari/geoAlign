###################################################################################
# Developed by Matthew Marcotullio, Matt Macari, Lily Yassemi, and Dylan Lucas    #
#             for California State Polytechnic University, Humboldt               #
###################################################################################

# Prints a report of the file processing status.
def print_output_statistics(num_files_processed, num_files_failed, failed_files, output_dir):
    print('\n\n-----------------------')
    print('\nFiles have been processed...')
    print(f'\nNumber of files successfully georeferenced: {num_files_processed - num_files_failed}')
    print(f'\nNumber of failed files: {num_files_failed}')
    
    if failed_files:
        print('\nFiles that failed during processing:\n')
        for each in failed_files:
            print(f'{each}\n')
    
    print('------------------------------------------------------------------------')
    print(f'Check {output_dir} for the results.')