import streamlit as st
import pandas as pd
import cvxpy as cp
import numpy as np


st.write("""
# Simple App for solving :
minimize ((x - y)**2)
subject to constraints : x + y = a,
                         x - y >= b
""")

st.sidebar.header('User Input Values for the Constraints')

def user_input_vals():
    a = st.sidebar.slider('Value of "a" in equality constraint', 1.0, 6.0, 1.0)
    b = st.sidebar.slider('Value of "b" in inequality constraint', 1.0, 6.0, 1.0)
    data = {'a': a,
            'b': b,}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_vals()

st.subheader('User Input Values for the Constraints')
st.write(df)

x = cp.Variable()
y = cp.Variable()
df = df.values

# Create two constraints.
constraints = [x + y == df[0][0],
               x - y >= df[0][1]]

# Form objective.
obj = cp.Minimize((x - y)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
# print("status:", prob.status)
# print("optimal value", prob.value)
# print("optimal var", x.value, y.value)

st.subheader('Problem Status')
st.write(prob.status)

st.subheader('Objective Value')
st.write(prob.value)
#st.write(prediction)

st.subheader('Optimal Value of x')
st.write(str(x.value))

st.subheader('Optimal Value of y')
st.write(str(y.value))

