
import streamlit as st
import pandas as pd
import random


#breakfast_inputs =list( st.text_input("Enter breakfast text"))
#lunch_inputs = list(st.text_input("Enter lunch text"))
#dinner_inputs = list( st.text_input("Enter dinner text"))


breakfast_inputs = st.text_input("Enter breakfast text").replace(' ', '_').split(',')
lunch_inputs = st.text_input("Enter lunch text").replace(' ', '_').split(',')
dinner_inputs = st.text_input("Enter dinner text").replace(' ', '_').split(',')


#breakfast_inputs = 'ferfef,feferf'.replace(' ', '_').split(',')
#lunch_inputs = 'ferfef,yhyhyj'.replace(' ', '_').split(',')
#dinner_inputs = 'ferfef,yhyhyj,defr'.replace(' ', '_').split(',')


breakfast_default = ["Aloo Pronthha", "Milk Meusli", "Poha", "Upma", "Ajwain Pronthha", "Suji Chila","Bread Omelette","Butter Toast & Milk"]
lunch_default = ["Dal Roti","Pulao", "Matar Paneer", "Rajma Rice"]
dinner_default = ["Dal", "Fish Curry with Rice", "Matar Paneer with Roti", "Veg Pulao", "Palak Paneer with Roti"]

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#check if provided length is less than days
if len(breakfast_inputs) < len(days):
    breakfast_inputs = breakfast_inputs + random.choices(breakfast_default, k = len(days)-len(breakfast_inputs))

if len(lunch_inputs) < len(days):
    lunch_inputs = lunch_inputs + random.choices(lunch_default, k = len(days)-len(lunch_inputs))

if len(dinner_inputs) < len(days):
    dinner_inputs = dinner_inputs + random.choices(dinner_default, k = len(days)-len(dinner_inputs))


breakfast_inputs = random.choices(breakfast_inputs, k = len(days))
lunch_inputs = random.choices(lunch_inputs, k = len(days))
dinner_inputs = random.choices(dinner_inputs, k = len(days))


df = pd.DataFrame({"Day":days,
                   "Breakfast":breakfast_inputs,
                   "Lunch":lunch_inputs,
                   "Dinner":dinner_inputs})

st.title('Meal Planner')

# Display the DataFrame
st.dataframe(df)