### Model Serve Backend
Fast API로 구현한 요르댕 프로젝트 백앤드

### 가상환경 설정
```shell
conda create --name yordang-backend python=3.10.4
conda env create --file environment.yaml
```

### 서버 실행
```shell
uvicorn main:app --reload
```