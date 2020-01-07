# GOE

### GOE란??
GOE는 Guardians Of Energy의 줄임말로, 전기요금을 실시간으로 예측 및 계산해 각 상황별 솔루션을 제공하는 스마트홈 케어 시스템입니다.  
android 환경에서 구동이 가능하며, 구동을 위해선 서버가 실행되어야 합니다.

### 개발 목적
여름철 외출할 때 에어컨을 켜놔서 전기요금이 엄청나게 나오게 되는, **소위 전기요금 폭탄** 이라는 말이 있습니다. 저희는 이러한 일이 일어나는 이유가 사용자가 현재 가전제품이 어떻게 가동되고 있는지 실시간으로 알기 어렵고, 이번 달에 얼마나 전기요금을 사용했는지를 모르기때문이라고 판단했습니다.  GOE는 이러한 문제점들을 해결해 에너지가 낭비되는것을 막기 위해 개발되었습니다.

### 사용 기술
GOE는 사용자의 가전제품 사용 패턴을 학습해 이를 예측하는 딥러닝 모델을 사용합니다. 모델은 월, 요일의 간단한 시간적 정보와 기온, 날씨(비, 맑음 등)의 날씨 정보를 필요로 하며 이를 기반으로 예측을 합니다.  
따라서 2019년 x월 x일에는 이렇게 행동했기 때문에 2020년의 같은 날에도 동일하게 행동할 것이다가 아닌, 사용자 패턴에 맞게 주말과 날씨까지 고려해서 예측을 하게 됩니다.

### 사용 라이브러리
#### APP
 * java
 * com.github.PhilJay:MpAndroidChart 3.0.2 ~

#### Server
 * tensorflow 2.0.0 ~
 * flask 1.1.1 ~
 * firebase_admin 3.2.0 ~
 



GOE는 실제 사용이 목적이 아닌, 프로토타입 개발을 목적으로 개발되었습니다. 따라서 현재 AI는 냉장고와 에어컨만 예측이 가능합니다.  
또한 서버가 돌아가야하기 때문에 개별적으로 실행이 불가능합니다.
