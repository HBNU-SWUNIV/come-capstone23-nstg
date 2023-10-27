# 한밭대학교 컴퓨터공학과 NSTG팀

**팀 구성**
- 20181587 김태현
- 20181594 이규호

## <u>Teamate</u> Project Background
- 드론 해킹 공격 현황  
  ![기사](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/121182760/e33e6234-01b9-493f-a2f5-62811af1240e)
  
- ### 필요성
  사람의 개입 없이 주행이 가능한 무인이동체에 대한 시장 수요가 급증함에 따라 관련 기술들이 주목받고 있다.  
  특히, 무인비행체 즉 드론은 물품 배송, 군사 목적 등 다양한 분야에서 폭넓게 활용되고 있는 만큼, 다양한 보안 이슈가 발생한다.  
  따라서, 무선네트워크의 드론 대상으로 하는 공격의 원리 및 구현 방법에 대한 체계적인 분석을 통해 대응방안을 마련할 필요가 있다.  
  그 중 Hijacking과 Evil Twin 공격은 인증해제와 연결지어 구현될 수 있기 때문에, 이러한 공격들의 시발점이 되는 인증해제 공격을 분석하여 대응 방안을 제안하고자 한다.
  
## System Design
  - ### System Requirements
    ![Evil Twin_Hijacking](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/7e5b14f8-c7f4-452d-8f4f-06935722df1b)
    - Evil Twin 공격 시 드론과 지상통제센터의 연결이 드론과 Rogue AP로 변환 되어야 함
    - Hijacking 공격 시 드론이 지상통제센터가 지시한 방향으로 이동 하지 않아야 함
    
    ![인증해제 탐지](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/121182760/daa52acd-5fd1-46c7-b40e-fab2052b40f7)  
    - 공격 도구에서 인증해제 공격이 구현되어 AP와 Client의 연결을 지속해서 해제할 수 있어야 함
    - sniffer가 Wi-Fi 네트워크에서 흐르는 모든 패킷 데이터를 저장할 수 있어야 함
    - 패킷 데이터를 csv 파일로 변환할 수 있어야 함
    - 패킷 데이터에서 인증해제 공격을 정확하게 검출할 수 있어야 함
    
## Case Study
  - ### Description
  
  
## Conclusion
  - 드론 네트워크 대상으로 하는 공격 Evil Twin, Hijacking 구현을 통한 위험성 확인
    - Evil Twin 공격으로 Rogue AP에 지상통제센터(GCS:Ground Control System)의 드론 통제권 탈취  
    ![Evil Twin](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/110e952d-4b1c-4ade-8cd2-e58bb427a52c)

    - Hijacking 공격으로 인해 주입 된 패킷으로 드론이 지상통제센터가 의도한 방향으로 이동 불가
    ![Hijacking](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/65a919a4-1933-4601-aba4-6c44245c0ebe)

  - Evil Twin, Hijacking 공격의 기반이 되는 인증해제 공격 분석
    
  - LSTM 모델을 이용한 인증해제 공격 탐지, 그로 인한 Evil Twin, Hijacking 공격 예방
    - LSTM 모델을 이용한 인증해제 공격 탐지율
    ![LSTM model](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/e8b5812d-68b5-4822-a0e1-8f20581afbd0)
  
## Project Outcome
- 한국통신학회 2023년 하계학술대회 "와이파이 기반 드론 네트워크에서 Evil Twin 공격 구현에 관한 연구"
![한국통신학회 2023년 하계학술대회_2](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/1f2b4fec-3789-465e-9393-9ee736b23b56)

- 한국통신학회 2023년 하계학술대회 "와이파이 기반 드론 네트워크에서 드론 하이재킹 구현에 관한 연구"
![한국통신학회 2023년 하계학술대회](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/01f1f1ee-1b59-40af-993e-04f0517f697a)

- 한국통신학회 2023년 하계학술대회 우수상 수상
![한국통신학회 2023년 하계학술대회_우수상](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/6e941bed-889f-458e-aee8-508d87947c90)

- 한국통신학회 2023년 추계학술대회 "LSTM 기반의 WiFi 인증 해제 공격 검출에 관한 연구"
![한국통신학회 2023년 추계학술대회](https://github.com/HBNU-SWUNIV/come-capstone23-nstg/assets/83878234/71a27872-1110-4b79-bd4d-3e766c7ab028)


