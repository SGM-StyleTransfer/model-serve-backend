from fastapi import FastAPI, File, UploadFile
import cv2

app = FastAPI()

@app.post("/uploadfiles/")
async def create_upload_files(
    original_video: UploadFile = File(description="Original Video"),
    key_frame: UploadFile = File(description="Key Frame Image"),
    reference_img: UploadFile = File(description="Reference Image"),
):
    # TODO: OpenCV로 이미지, 비디오 파일을 띄우기
    # 입력 받은 파일 생성    
    print(type(key_frame.file))
    
    f = open(key_frame.filename, "bw")
    f.write(key_frame.file.read())
    f.close()

    # 해당 이미지 파일 읽고 띄우기
    key_frame = cv2.imread(key_frame.filename, cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', key_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Model Prediction

    # 

    return {"output_video": "hello world"}