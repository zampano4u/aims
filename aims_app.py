import streamlit as st

def calculate_aims_score(responses):
    # 항목 1-7의 점수만 합산
    scores = [int(resp.split('(')[1].split(')')[0]) for resp in responses[:7]]
    total_score = sum(scores)
    
    # 임상적 해석
    if (len([score for score in scores if score >= 2]) >= 2) or (max(scores) >= 3):
        interpretation = "Suggests the presence of TD"
    elif len([score for score in scores if score == 2]) == 1:
        interpretation = "Mild abnormal movements present"
    else:
        interpretation = "No TD-related abnormal movements"
    
    return total_score, interpretation

def translate_to_english(questions, responses):
    eng_questions = [
        "Muscles of Facial Expression (forehead, eyebrows, periorbital area, cheeks, frowning, blinking, smiling, grimacing, etc.)",
        "Lips and Perioral Area (puckering, pouting, smacking, etc.)",
        "Jaw (biting, clenching, chewing, mouth opening, lateral movement, etc.)",
        "Tongue (rate only increases in movement both in and out of mouth, not inability to sustain movement)",
        "Upper (arms, wrists, hands, fingers) (include choreic movements, athetoid movements, do not include tremor)",
        "Lower (legs, knees, ankles, toes) (lateral knee movement, foot tapping, heel dropping, foot squirming, etc.)",
        "Neck, shoulders, hips (rocking, twisting, squirming, pelvic gyrations, etc.)",
        "Severity of abnormal movements overall",
        "Incapacitation due to abnormal movements",
        "Patient's awareness of abnormal movements",
        "Current problems with teeth and/or dentures",
        "Does the patient usually wear dentures?"
    ]
    
    # 응답 번역 매핑
    response_translations = {
        "No dyskinesia(0)": "No dyskinesia(0)",
        "Minimal dyskinesia(1)": "Minimal dyskinesia(1)",
        "Mild dyskinesia(2)": "Mild dyskinesia(2)",
        "Moderate dyskinesia(3)": "Moderate dyskinesia(3)",
        "Severe dyskinesia(4)": "Severe dyskinesia(4)",
        "None(0)": "None(0)",
        "Minimal(1)": "Minimal(1)",
        "Mild(2)": "Mild(2)",
        "Moderate(3)": "Moderate(3)",
        "Severe(4)": "Severe(4)",
        "No awareness(0)": "No awareness(0)",
        "Aware, no distress(1)": "Aware, no distress(1)",
        "Aware, mild distress(2)": "Aware, mild distress(2)",
        "Aware, moderate distress(3)": "Aware, moderate distress(3)",
        "Aware, severe distress(4)": "Aware, severe distress(4)",
        "No(0)": "No(0)",
        "Yes(1)": "Yes(1)"
    }
    
    # 번역된 응답 목록 생성
    eng_responses = [response_translations.get(resp, resp) for resp in responses]
    
    return eng_questions, eng_responses

def main():
    st.title("AIMS (Abnormal Involuntary Movement Scale) 평가 도구")
    
    st.write("다음 항목에 대해 평가해주세요:")
    
    questions = [
        "1. 얼굴 표정 근육 (이마, 눈썹, 눈 주변 부위, 뺨의 움직임, 찡그림, 눈 깜빡임, 미소, 얼굴 찡그림 등)",
        "2. 입술과 입 주변 부위 (입술 오므리기, 뾰루퉁한 표정, 입맛 다시기 등)",
        "3. 턱 (물기, 이 악물기, 씹기, 입 벌리기, 옆으로 움직이기 등)",
        "4. 혀 (입 안팎으로 움직임이 증가한 경우만 평가, 지속적인 움직임 불능은 평가하지 않음)",
        "5. 상지(팔, 손목, 손, 손가락) (무도병적 움직임, 무정위 운동 포함, 진전은 포함하지 않음)",
        "6. 하지(다리, 무릎, 발목, 발가락) (무릎의 측면 움직임, 발 두드리기, 발꿈치 떨어뜨리기, 발 꿈틀거림 등)",
        "7. 목, 어깨, 엉덩이 (흔들기, 비틀기, 꿈틀거림, 골반 회전 등)",
        "8. 비정상적 움직임의 전반적 심각도",
        "9. 비정상적 움직임으로 인한 기능 장애",
        "10. 환자의 비정상적 움직임에 대한 인식",
        "11. 치아 및/또는 의치 관련 현재 문제",
        "12. 환자가 일반적으로 의치를 착용하는지 여부"
    ]
    
    response_options = [
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["No dyskinesia(0)", "Minimal dyskinesia(1)", "Mild dyskinesia(2)", "Moderate dyskinesia(3)", "Severe dyskinesia(4)"],
        ["None(0)", "Minimal(1)", "Mild(2)", "Moderate(3)", "Severe(4)"],
        ["None(0)", "Minimal(1)", "Mild(2)", "Moderate(3)", "Severe(4)"],
        ["No awareness(0)", "Aware, no distress(1)", "Aware, mild distress(2)", "Aware, moderate distress(3)", "Aware, severe distress(4)"],
        ["No(0)", "Yes(1)"],
        ["No(0)", "Yes(1)"]
    ]
    
    responses = []
    
    # 항목 1-12 응답 수집
    for i in range(12):
        st.subheader(questions[i])
        response = st.radio(
            f"항목 {i+1}의 응답:",
            options=response_options[i],
            key=f"q{i+1}"
        )
        responses.append(response)
    
    if st.button("결과 계산"):
        total_score, interpretation = calculate_aims_score(responses)
        
        # 영어로 번역
        eng_questions, eng_responses = translate_to_english(questions, responses)
        
        # 결과 출력 형식 생성 (영어로만)
        result_text = "**Abnormal Involuntary Movement Scale, AIMS**\n\n"
        
        # 각 항목의 응답 추가
        for i in range(12):
            result_text += f"{i+1}. {eng_questions[i]} {eng_responses[i]}\n"
        
        # 총점과 해석 추가
        result_text += f"\nTotal Score: {total_score}\n"
        result_text += f"Clinical Interpretation: {interpretation}"
        
        # 결과 표시 (영어로만)
        st.subheader("Assessment Results (English)")
        st.code(result_text, language=None)
        st.info("To copy the results, click the copy icon in the top right corner of the code block.")

if __name__ == "__main__":
    main()

