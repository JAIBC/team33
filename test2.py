import streamlit as st
from joblib import load


# BMI에 따라 비만도를 계산하는 함수
def obesity(bmi):
    if bmi <= 18.5:
        return 0 # 저체중
    elif bmi < 25:
        return 1 # 정상
    elif bmi < 30:
        return 2 # 과체중
    elif bmi < 35:
        return 3 # 1단계 비만
    elif bmi < 40:
        return 4 # 2단계 비만
    else:
        return 5 # 3단계 비만

def main():
    st.title("당뇨병 의심 여부 예측")
    st.write("아래 정보를 입력하여 당뇨병 의심 여부를 확인하세요.")

    # 모델 불러오기
    model = load('sgd_model.joblib')

    HighBP = st.number_input("고혈압이 있으면 1 없으면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    HighChol = st.number_input("콜레스트롤 수치가 높으면 1 정상이면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    CholCheck = st.number_input("5년내에 콜레스트롤을 체크해본적이 있다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    bmi = st.number_input("BMI를 입력해주세요.", min_value=0.0)
    obesity_level = obesity(bmi)
    Smoker = st.number_input("평생 100개 이상의 담배를 피운적이 있으면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    Stroke = st.number_input("뇌졸중을 경험해보았다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    HeartDiseaseorAttack = st.number_input("심장질환이나 심근경색을 가지고 있다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    PhysActivity = st.number_input("최근 30일간 직장활동외에 신체활동을 했다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    Fruits = st.number_input("하루에 과일을 1회 이상 섭취하면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    Veggies = st.number_input("하루에 채소를 1회 이상 섭취하면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    HvyAlcoholConsump = st.number_input("성인 남성의 경우 주당 14잔 성인 여성의 경우 주당 7잔 이상 마신다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    AnyHealthcare = st.number_input("건강보험을 포함한 들고있는 의료보험이 있다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    NoDocbcCost = st.number_input("지난 1년동안 비용때문에 병원에 가야했지만 갈 수 없었던 적이 있다면 1 아니면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    GenHlth = st.number_input("일반적으로 자신의 건강을 어떻게 생각하는가? 1.훌륭함 2.매우 좋음 3.양호함 4.보통 5.나쁨", min_value=1, max_value=5, step=1)
    PhysHlth = st.number_input("지난 30일 동안 신체적 질병이나 부상 문제를 포함한 신체 건강 문제 일 수를 입력해주세요.", min_value=0, max_value=30, step=1)
    Sex = st.number_input("남성이면 1 여성이면 0을 입력해주세요.", min_value=0, max_value=1, step=1)
    Age = st.number_input("나이 범위 번호를 입력해주세요. 1.(18-24) 2.(25-29) 3.(30-34) 4.(35-39) 5.(40-44) 6.(45-49) 7.(50-54) 8.(55-59) 9.(60-64) 10.(65-69) 11.(70-74) 12.(75-79) 13.(80이상)", min_value=1, max_value=13, step=1)
    Education = st.number_input("학력을 입력해주세요.\n1.(학교를 다니지 않았거나 유치원만) \n2.(초등) \n3.(중등) \n4.(고등학교 일부) \n5.(고등학교 졸업 또는 검정고시, 대학1년~3년) \n6.(대학4년이상)", min_value=1, max_value=6, step=1)
    Income = st.number_input("소득 범위를 입력해주세요.1: $10,000 미만 2: $10,000 -$14,999 3: $15,000 - $19,999 4: $20,000 - $24,999 5: $25,000 - $34,999 6: $35,000 - $49,999 7: $50,000 - $74,999 8: $75,000 이상",min_value=1, max_value=8, step=1)

    
    if st.button("예측하기"):

        user_info_processed = [[HighBP, HighChol, CholCheck, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, PhysHlth, Sex, Age, Education, Income, obesity_level]]
        
        prediction = model.predict(user_info_processed)
        
        if prediction == 1:
            st.write("당뇨병이 의심됩니다.")
        else:
            st.write("당뇨병이 의심되지 않습니다.")

if __name__ == "__main__":
    main()
