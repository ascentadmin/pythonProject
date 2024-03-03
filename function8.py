def orgafile_by_format():
    import os
    import shutil

    source_dir = r"C:\Users\USER\Downloads"
    base_dest_dir = r"C:\Users\USER\Downloads\정리"

    print(f"Source Directory: {source_dir}")
    print(f"Destination Base Directory: {base_dest_dir}")

    dest_dirs = {
        'images': os.path.join(base_dest_dir, '이미지'),
        'documents': os.path.join(base_dest_dir, '문서'),
        'videos': os.path.join(base_dest_dir, '비디오'),
        'others': os.path.join(base_dest_dir, '기타'),
    }

    for dir in dest_dirs.values():
        if not os.path.exists(dir):
            os.makedirs(dir)
            print(f"Created directory: {dir}")

    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        _, file_ext = os.path.splitext(file_name)

        if file_ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            dest_dir = dest_dirs['images']
        elif file_ext.lower() in ['.pdf', '.doc', '.docx', '.txt']:
            dest_dir = dest_dirs['documents']
        elif file_ext.lower() in ['.mp4', '.avi', '.mov']:
            dest_dir = dest_dirs['videos']
        else:
            dest_dir = dest_dirs['others']

        print(f"Moving {file_name} to {dest_dir}")
        shutil.move(file_path, os.path.join(dest_dir, file_name))

orgafile_by_format()
