import streamlit as st
import pickle
import numpy as np

#model = pickle.load(open('model5.pkl','rb'))
pickle_in = open("model5.pkl","rb")
model=pickle.load(pickle_in)


def predict_test(DMV_Test_1,DMV_Test_2):
#    input = np.array([[DMV_Test_1,DMV_Test_2]]).astype(np.float64)
    prediction=model.predict(np.array([[DMV_Test_1,DMV_Test_2]]).astype(np.float64))
#    prediction = model.predict(input)
    #pred='{0:.{1}f}'.format(prediction[0][0],1)
    print(prediction)
    return prediction

def main():
#    st.title("STREAMLIT TUTORIAL")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit DMV_TEST_RESULT </h2>
    </div>

"""
       #<div style="background-color:#F4D03F;padding:10px >
       #<h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       #</div>

    st.markdown(html_temp,unsafe_allow_html=True)

    DMV_Test_1=st.text_input("Dmv_test1","Type here")
    DMV_Test_2=st.text_input("Dmv_test2","Type here")
    result=""
    if st.button("Predict"):
        result=predict_test(DMV_Test_1,DMV_Test_2)
    if result == 1:
    #st.success('The output is {}'.format(result))
        st.success("The output is PASS")
    if result==0:
        st.success("The output is FAIL")





if __name__=='__main__':
    main()
