import os
import shutil

source_dir = r"C:\Users\USER\Downloads"
dest_dir = r"C:\Users\USER\Downloads\정리"

# source_dir 내의 각 파일에 대해 반복
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)  # 파일의 전체 경로를 생성
    file_size = os.path.getsize(file_path)  # 파일 사이즈를 바이트 단위로 가져오기
    file_size_mb = file_size / (1024 * 1024)  # 바이트를 메가바이트로 변환

    # 파일 사이즈가 10MB 이상인 경우, 파일을 dest_dir로 이동
    if file_size_mb >= 10:
        shutil.move(file_path, dest_dir)

# git에 수정본 커밋
