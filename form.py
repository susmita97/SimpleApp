import streamlit as st
import streamlit.components.v1 as components
    
def app():

    st.title('Check your Approval for Home Buying')
    st.write('Please enter some information below')
    st.write('The system will predict if you are currently eligible for approval')
    
    st.write('All are required fields')

    form = st.form(key='my_form')
    GrossMonthlyIncome = form.number_input(label='Gross Monthly Income', min_value=10)
    CreditCardPayment = form.number_input(label='Credit Card Payment', min_value=0)
    CarPayment = form.number_input(label='Car Payment',min_value=0)
    StudentLoanPayments = form.number_input(label='Student Loan Payments',min_value=0)
    AppraisedValue = form.number_input(label='Appraised Value',min_value=0)
    DownPayment = form.number_input(label='Down Payment',min_value=0)
    LoanAmount = form.number_input(label='Loan Amount',min_value=0)
    MonthlyMortgagePayment = form.number_input(label='Monthly Mortgage Payment',min_value=0)
    #CreditScore = form.slider(label="Credit Score",key = "CreditScore", min_value=0, max_value=1500)
    CreditScore = 650
    
    submit_button = form.form_submit_button(label='Submit')

    if submit_button:

        if CreditScore > 640:

            loanbalance = AppraisedValue-DownPayment
            ltv = (loanbalance/AppraisedValue)*100

            if ltv > 80:
               pmi = AppraisedValue/100

            temp = pmi + CreditCardPayment+CarPayment+StudentLoanPayments+MonthlyMortgagePayment
            dti = (temp / GrossMonthlyIncome)*100

            if dti <= 43:
               fedti = ((temp-MonthlyMortgagePayment-pmi)/GrossMonthlyIncome)*100

               if fedti <= 28 and itv < 95: 

                  st.write('Approved!')
                  st.write('You are ready to buy a home! Yayy!!!!')
                  st.write('A good resource: https://www.hud.gov/topics/buying_a_home')
                  st.write('The U.S. Department of Housing and Urban Development has all the resources that a first time house buyer needs!')

               else:
                    st.write('Oh no not approved.')
                    st.write('Your FEDTI score is too high, normally it should be less than or equal to 28%')
                    st.write('A common suggestion would be to increase your down payment amount, or look for a less expensive home')
                    st.write('Consider to continue renting while saving more for a down payment')
                    st.write('A good resource: https://www.hud.gov/topics/buying_a_home')
                    st.write('The U.S. Department of Housing and Urban Development has all the resources that a first time house buyer needs!')

            else:
                 st.write('Oh no not approved.')
                 st.write('Your DTI is too high, normally it should be less than or equal to 28%')
                 st.write('A common suggestion would be to pay off some current debt or transfer debt to a lower interest rate loan / credit card')
                 st.write('A good resource: https://www.hud.gov/topics/buying_a_home')
                 st.write('The U.S. Department of Housing and Urban Development has all the resources that a first time house buyer needs!')

        else:
            st.write('Your Credit Score is too low')
            st.write('A common suggestion would be to wait for some time to buy an expensive property')
            st.write('A good resource: https://www.hud.gov/topics/buying_a_home')
            st.write('The U.S. Department of Housing and Urban Development has all the resources that a first time house buyer needs!')
