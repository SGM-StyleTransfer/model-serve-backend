from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi.responses import StreamingResponse
from tqdm import tqdm

app = FastAPI()

# 파일 데이터를 nd array로 변환
def load_img_into_np_array(data):
    return np.array(Image.open(BytesIO(data)))

@app.post("/api/uploadfiles/")
async def upload_files (
    original_video: UploadFile = File(description="Original Video"),
    key_frame: UploadFile = File(description="Key Frame Image"),
    reference_img: UploadFile = File(description="Reference Image"),
    mask_img: UploadFile = File(description="Mask Image"),
):
    # 받은 file을 numpy의 ndarray로 변환
    # 비디오 파일은 모델에서 어떤 타입으로 사용되는지 확인 필요
    key_frame = load_img_into_np_array(await key_frame.read())    
    reference_img = load_img_into_np_array(await reference_img.read())
    mask_img = load_img_into_np_array(await mask_img.read())

    # 변환한 ndarray를 openCV로 확인
    # cv2.imshow('image', swaped_reference_img)
    # cv2.waitKey(50)
    # cv2.destroyAllWindows()

    ###############################################################
    # TODO: 여기에 모델 추가
    # Read video file & convert into generator
    # def iterfile():
    #     yield from original_video.file 
    fourcc = cv2.VideoWriter_fourcc(*'H264')        # TODO: 비디오 생성 코덱을 반드시 'H264'로 설정해주셔야 합니다 !!
    cap = cv2.VideoCapture()
    cap.open('../samples/Cat.mp4')
    videoWriter = cv2.VideoWriter('../samples/ResultCat.mp4', fourcc, int(cap.get(cv2.CAP_PROP_FPS)), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    all_f = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    for i in tqdm(range(int(all_f))):
        ret, frame = cap.read()
        videoWriter.write(frame)
    cap.release()
    videoWriter.release()
    ###############################################################

    return 'Complete converting video.'


## 비디오 변환 후 완료된 result video를 streaming 하는 get API
@app.get('/api/get-result/')
async def get_result_video():

    def iterfile():
        output_video_path = '../samples/ResultCat.mp4' # 원하는 파일 경로로 변경
        with open(output_video_path, mode='rb') as file_like:
            yield from file_like

    # return video object
    return StreamingResponse(iterfile(), media_type='video/mp4')
