import os
from django.utils import timezone

def user_directory_path(instance, filename):
    # Generate a unique folder name based on the current timestamp and user ID
    user_id = instance.uploader.id
    folder_name = f'user_{user_id}'
    
    # Check if the file already exists
    file_path = os.path.join('assets/files', folder_name, filename)
    if os.path.exists(file_path):
        # Split the filename and extension
        name, ext = os.path.splitext(filename)
        
        # Add "1" to the filename
        new_filename = f"{name}1{ext}"
        
        # Generate a new file path
        new_file_path = os.path.join('assets/files', folder_name, new_filename)
        
        # Update the file path
        file_path = new_file_path
    
    return file_path

