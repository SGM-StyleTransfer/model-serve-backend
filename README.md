### Model Serve Backend
Fast API로 구현한 요르댕 프로젝트 백앤드

### 가상환경 설정
```shell
conda env create --file environment.yaml
```

### 서버 실행
```shell
cd src  # src 디렉토리로 이동
uvicorn main:app --reload
```