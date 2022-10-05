from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

# 파일 데이터를 nd array로 변환
def load_img_into_np_array(data):
    return np.array(Image.open(BytesIO(data)))

@app.post("/api/uploadfiles/")
async def upload_files_and_return_video (
    original_video: UploadFile = File(description="Original Video"),
    key_frame: UploadFile = File(description="Key Frame Image"),
    reference_img: UploadFile = File(description="Reference Image"),
    mask_img: UploadFile = File(description="Mask Image"),
):
    # 받은 file을 numpy의 ndarray로 변환
    # 비디오 파일은 모델에서 어떤 타입으로 사용되는지 확인 필요
    key_frame = load_img_into_np_array(await key_frame.read())
    swaped_key_frame = cv2.cvtColor(key_frame, cv2.COLOR_BGR2RGB)
    
    reference_img = load_img_into_np_array(await reference_img.read())
    swaped_reference_img = cv2.cvtColor(reference_img, cv2.COLOR_BGR2RGB)
    
    mask_img = load_img_into_np_array(await mask_img.read())
    swaped_mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB)

    # 변환한 ndarray를 openCV로 확인
    # cv2.imshow('image', swaped_reference_img)
    # cv2.waitKey(50)
    # cv2.destroyAllWindows()

    # TODO: Request model to generate a video

    # Read video file & convert into generator
    def iterfile():
        yield from original_video.file        
    
    # return video object
    return StreamingResponse(iterfile(), media_type='video/mp4')