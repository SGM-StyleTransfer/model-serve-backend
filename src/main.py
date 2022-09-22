from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

app = FastAPI()

# 파일 데이터를 nd array로 변환
def load_img_into_np_array(data):
    return np.array(Image.open(BytesIO(data)))

# nd array의 b, r 채널 swap
def swap_red_blue_of_np_array(image_array):
    r = image_array[:, :, 0].copy()
    b = image_array[:, :, 2].copy()
    image_array[:, :, 0] = b
    image_array[:, :, 2] = r

    return image_array

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
    swaped_key_frame = swap_red_blue_of_np_array(key_frame)
    
    reference_img = load_img_into_np_array(await reference_img.read())
    swaped_reference_img = swap_red_blue_of_np_array(reference_img)
    
    mask_img = load_img_into_np_array(await mask_img.read())
    swaped_mask_img = swap_red_blue_of_np_array(mask_img)

    # 변환한 ndarray를 openCV로 확인
    cv2.imshow('image', swaped_reference_img)
    cv2.waitKey(50)
    cv2.destroyAllWindows()

    # TODO: Request model to generate a video

    return {"output_video": "something new video file"}