import featuretools as ft
import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

data = ft.demo.load_mock_customer()
customers_df = data["customers"]
customers_df