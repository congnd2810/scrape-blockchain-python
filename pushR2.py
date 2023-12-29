import glob
import boto3
from multiprocessing import Pool
import os

bucket = "articles-blockchain"
s3 = boto3.client('s3',
                  endpoint_url='https://6991066063047aece804c8592b9c2abc.r2.cloudflarestorage.com',
                  aws_access_key_id='455a686bffe601ce063546652458ccfc',
                  aws_secret_access_key='bd0a281fb48108d78f2499f43101c9d7ab233459c0baaffd104c69b10a3c951a'
                  )


def uploadFile(info):
    localFilePath, r2FilePath = info[0], info[1]
    print(localFilePath, r2FilePath)
    s3.upload_file(localFilePath, bucket, r2FilePath)


def uploadFolder(localFolderPath, r2FolderPath):
    files = glob.glob(f'{localFolderPath}/*')
    files = [i.replace('\\', '/') for i in files]
    print(localFolderPath, r2FolderPath)
    p = Pool(20)
    input = [(file, f'{r2FolderPath}/{file[20:]}') for file in files]
    print(input)
    p.map(uploadFile, input)
    p.terminate()


# def uploadR2(img, name):
#     s3.put_object(Bucket=bucket, Key=name,
#                   Body=cv2.imencode(".jpg", img)[1].tobytes())
#     return [name]
# s3.upload_file("imageXTPNpRm9Jfs.png", bucket, "imageXTPNpRm9Jfs.png")


if __name__ == '__main__':
    uploadFolder('./dataHtmlMarginAtm/*/*', 'marginAtm')

    # remove all objects from bucket
    # objects_to_delete = []
    # response = s3.list_objects_v2(Bucket=bucket)
    # for obj in response.get('Contents', []):
    #     objects_to_delete.append({'Key': obj['Key']})

    # # Kiểm tra xem có đối tượng nào để xóa hay không
    # if objects_to_delete:
    #     # Xóa tất cả các đối tượng trong bucket
    #     s3.delete_objects(Bucket=bucket, Delete={'Objects': objects_to_delete})
    #     print(f"Tất cả các đối tượng trong bucket {bucket} đã được xóa.")
    # else:
    #     print(f"Bucket {bucket} đã trống, không có đối tượng để xóa.")
