datafields = r"../data/datafields.csv"

nav_image = r"../data/Logo_UIT.jpg"
home_image = r"../data/home.jpg"

quarter_1 = r"../data/q1.csv"
quarter_2 = r"../data/q2.csv"
quarter_3 = r"../data/q3.csv"
quarter_4 = r"../data/q4.csv"

quarter_1_datasales = r"../data/q1_datesales.csv"
quarter_2_datasales = r"../data/q2_datesales.csv"
quarter_3_datasales = r"../data/q3_datesales.csv"
quarter_4_datasales = r"../data/q4_datesales.csv"

features = ["DayOfWeek","Customers", "Promo", "StateHoliday", "SchoolHoliday", "StoreType", "Assortment", "CompetitionDistance", 
            "CompetitionOpenSinceMonth","Promo2SinceWeek", "PromoInterval", "MonthName"]
salesDependingFeatures = [3,319,0,0,0,3,2,5350.00,4.00,22.00,2,6]
model_load = r"../model/sales_prediction.sav"
