from fastapi import FastAPI, File, UploadFile
import cv2

app = FastAPI()

@app.post("/api/uploadfiles/")
async def create_upload_files(
    original_video: UploadFile = File(description="Original Video"),
    key_frame: UploadFile = File(description="Key Frame Image"),
    reference_img: UploadFile = File(description="Reference Image"),
    mask_img: UploadFile = File(description="Mask Image"),
):
    # TODO: 받은 file을 numpy나 torch를 사용해서 tensor로 변환하기  
    # 변환한 tensor를 openCV로 확인하기  

    print(original_video.filename)
    print(key_frame.filename)
    print(reference_img.filename)
    print(mask_img)

    # f = open(key_frame.filename, "bw")
    # f.write(key_frame.file.read())
    # f.close()

    # 해당 이미지 파일 읽고 띄우기
    # key_frame = cv2.imread(key_frame.filename, cv2.IMREAD_UNCHANGED)
    # cv2.imshow('image', key_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Model Prediction

    # 

    return {"output_video": "hello world"}