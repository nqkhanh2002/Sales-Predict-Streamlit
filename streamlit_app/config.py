datafields = "../data/datafields.csv"

nav_image = "data/Logo_UIT.jpg"
home_image = "data/home.jpg"

quarter_1 = "data/q1.csv"
quarter_2 = "data/q2.csv"
quarter_3 = "data/q3.csv"
quarter_4 = "data/q4.csv"

quarter_1_datasales = "data/q1_datesales.csv"
quarter_2_datasales = "data/q2_datesales.csv"
quarter_3_datasales = "data/q3_datesales.csv"
quarter_4_datasales = "data/q4_datesales.csv"

features = ["DayOfWeek","Customers", "Promo", "StateHoliday", "SchoolHoliday", "StoreType", "Assortment", "CompetitionDistance", 
            "CompetitionOpenSinceMonth","Promo2SinceWeek", "PromoInterval", "MonthName"]
salesDependingFeatures = [3,319,0,0,0,3,2,5350.00,4.00,22.00,2,6]
model_load = "../model/sales_prediction.sav"
