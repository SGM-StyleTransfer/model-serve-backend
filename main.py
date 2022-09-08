from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfiles/")
async def create_upload_files(
    original_video: UploadFile = File(description="Original Video"),
    key_frame: UploadFile = File(description="Key Frame Image"),
    reference_img: UploadFile = File(description="Reference Image"),
):
    # TODO: OpenCV로 이미지, 비디오 파일을 띄우기

    print(original_video.file)
    print(key_frame)
    print(reference_img)
    return {"output_video": "hello world"}