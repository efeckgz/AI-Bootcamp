import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

lr = LinearRegression()

df = pd.read_excel('cars.xls')

x = df.drop('Price', axis=1) # Everything but price
y = df[['Price']] # Price only

x_train, x_test, y_train, y_test = tts(x, y, random_state=42, test_size=.2)

preprocessor = ColumnTransformer(
    transformers= [
        ('num', StandardScaler(), ['Mileage', 'Cylinder', 'Liter', 'Doors']),
        ('cat', OneHotEncoder(), ['Make', 'Model', 'Trim', 'Type'])
    ]
)

pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', lr)])

pipeline.fit(x_train, y_train)
pred = pipeline.predict(x_test)

rmse = mean_squared_error(pred, y_test) ** 0.5
r2 = r2_score(pred, y_test)

def price_pred(make, model, trim, mileage, type, cylinder, liter, doors, sound, leather):
    input_data = pd.DataFrame({
        'Make': [make],
        'Model': [model],
        'Trim': [trim],
        'Mileage': [mileage],
        'Type': [type],
        'Cylinder': [cylinder],
        'Liter': [liter],
        'Doors': [doors],
        'Sound': [sound],
        'Leather': [leather]
    })


    return pipeline.predict(input_data)[0][0]

if __name__ == '__main__':
    st.title('Car Price Predictor :car:')
    st.write('This app uses a linear regression model to predict the price of a car based on the input features.')

    st.write("Enter car details to predict the price")
    make = st.selectbox('Make', df['Make'].unique())
    model = st.selectbox('Model', df.loc[df['Make'] == make]['Model'].unique())
    trim = st.selectbox('Trim', df.loc[df['Model'] == model]['Trim'].unique())
    mileage = st.number_input('Mileage', df['Mileage'].min(), df['Mileage'].max(), step=1000)
    type = st.selectbox('Type', df.loc[df['Model'] == model]['Type'].unique())
    cylinder = st.selectbox('Cylinder', df['Cylinder'].unique())
    liter = st.number_input('Liter', df['Liter'].min(), df['Liter'].max(), step=0.2)
    doors = st.selectbox('Doors', df['Doors'].unique())
    sound = st.checkbox('Sound')
    leather = st.checkbox('Leather')
    cruie = st.checkbox('Cruise')

    if st.button('Predict'):
        price = price_pred(make, model, trim, mileage, type, cylinder, liter, doors, sound, leather)
        st.write(f'Predicted Price: ${price:.2f}')
        st.write(f'RMSE: {rmse:.2f}')
        st.write(f'R2 Score: {r2:.2f}')
