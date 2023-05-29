# Yolov8 진행보고 (05/29)

Created: April 15, 2023 7:10 PM
Updated: May 29, 2023 2:29 PM

**관련 연구 논문**

- 300장 강아지 질환 이미지 사용
- Training: 80% , Validation : 10%, Test: 10%
- Conv2D model
- Accuracy: 0.9863 , Loss: 0.0137

> [https://www.researchgate.net/profile/Lokesha-Weerasinghe/publication/365929081_Intelligent_System_for_Skin_Disease_Detection_of_Dogs_with_Ontology_Based_Clinical_Information_Extraction/links/63aacdc403aad5368e45749d/Intelligent-System-for-Skin-Disease-Detection-of-Dogs-with-Ontology-Based-Clinical-Information-Extraction.pdf](https://www.researchgate.net/profile/Lokesha-Weerasinghe/publication/365929081_Intelligent_System_for_Skin_Disease_Detection_of_Dogs_with_Ontology_Based_Clinical_Information_Extraction/links/63aacdc403aad5368e45749d/Intelligent-System-for-Skin-Disease-Detection-of-Dogs-with-Ontology-Based-Clinical-Information-Extraction.pdf)
> 

### Yolov8 POSE 추가학습 사전내용

- Yolo는 Single Stage Method 로서 이미지 내에 존재하는 객체와 위치를 한번만 보고 예측함.

따라서 이전의 모델들에 비해 상대적으로 빠르며 실시간으로 객체를 탐지 할 수 있음.

→ 실시간 객체탐지 모델 중 경량화 장점을 보이는 MobileNet과 비교하기에 적합한 모델이라 판단하여 선정함.

- Ultralytics에서 개발된 모델. 기존 버전과 다르게 이미지 분류 모델을 학습하기 위한 통합 프레임워크로서 출시됨. 이전 버전에 비해서 성능과 속도에서 차이를 보임.
- DarkNet Backbone
- yolov8n Dataset Pretrained Model 을 이용하여 Custom Train 가능.
    - [Train Custom Data 참고](https://docs.ultralytics.com/yolov5/train_custom_data/)

### Dataset

- AIHUB 반려동물 피부질환 데이터
    - 반려동물 10,000마리 이상 (반려견 7종, 반려묘 4종 )
    - 질환 이미지 (Train : 55,874 / Validation :  6,985)

### Data Preprocessing

- Coco Data Format (x, y, width, height) 를 Yolo Data Format 에 맞게 Normalization(min, max center point calculated) 수행

![Untitled](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/Untitled.png)

![( 예시 코드)](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/Untitled%201.png)

( 예시 코드)

**(전처리 수행 전→ JSON File (left x, left h, image width, image height))**

![Untitled](https://github.com/dongheecha/pet-skin-disease/blob/main/Yolov8%20%EC%A7%84%ED%96%89%EB%B3%B4%EA%B3%A0%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/Untitled 2.png)

**(전처리 수행 후→ TXT File (center x, center y, w, h))**

![Untitled](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/Untitled%203.png)

### Training (현재 진행중)

- **Train dataset** : 55,874 (image, label)
- **Valid dataset**: 6,985 (image, label)
- **Class**: 6 (강아지 질환 5, 고양이 질환 1)
- **Batch size** : 10 **(10이 넘어가면 GPU 메모리 문제 발생)**
- **Epochs** : 20,
- **Learning late** : 0.01 **(Yolov8 기본값**)
- **image size** : 1920, 1080  **(AIHUB 모든 이미지 데이터가 1920, 1080으로 같음. Crop 사용 안함.)**
- 학습 라벨링 이미지
    
    ![val_batch0_labels.jpg](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/val_batch0_labels.jpg)
    

### 학습 결과

- 전체 성능 지표

![results.png](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/results.png)

- Precision-Recall Curve
    
    ![PR_curve.png](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/PR_curve.png)
    
- Recall-Confidence Curve
    
    ![R_curve.png](Yolov8%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A2%E1%86%BC%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%20(05%2029)%209f27e751ae0947bf90d43b06c7660ad2/R_curve.png)
