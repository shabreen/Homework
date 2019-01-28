#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Heroes of Pymoli Data Analysis
- While the people in the age group 20-24 had the highest Total Purchase Value, \$950.59, they did not spend the most on average. The people in the age group 40+ spent the most on average, \$4.68, whereas the people in age group 20-24 spent \$4.13.
- The item Retribution Axe was the most profitable item selling a total of \$37.26 even though it did not have the highest item price. This could be based on the stats of each item.  
- Although there was the greatest number of males in the data set, the people listed in the Other/Non-Disclosed gender had the highest average purchase price.


# In[ ]:


```python
# Dependencies
import pandas as pd
import numpy as np
```


# In[ ]:


```python
# File path
file = 'Resources/purchase_data.json'
```


# In[ ]:


```python
df = pd.read_json(file)
```


# In[ ]:


# Player Count


```python
player_count = len(df["SN"].value_counts())
pd.DataFrame([player_count], columns = ["Total Players"])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




# In[ ]:


# Purchasing Analysis (Total)


```python
# Finding & Appending Number of Unique Items
unique_items = len(df["Item ID"].value_counts())

# Total money spent
total_revenue = round(df["Price"].sum(), 2)

# Number of purchases
num_purchases = df["Price"].count()

# Average Price
average_price = round(df["Price"].mean(), 2)

# List for analysis
purchase_analysis = []

# Appending values to list
purchase_analysis.append(unique_items)
purchase_analysis.append("$" + str(average_price))
purchase_analysis.append(num_purchases)
purchase_analysis.append("$" + str(total_revenue))

# Converting to a DataFrame
pd.DataFrame([purchase_analysis], columns = ["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>


# In[ ]:


# Top Spenders


```python
df3 = df[["SN","Price","Item Name"]]
total_spent = df3.groupby("SN").sum()
total_spent.sort_values(by = "Price", ascending = False, inplace = True)

# Top Spender SN
names = list(total_spent.index.values)
top_names = [names[0],names[1],names[2],names[3],names[4]]

# Total Purchase Values
total_purchase_values_1 = total_spent.iloc[0,0]
total_purchase_values_2 = total_spent.iloc[1,0]
total_purchase_values_3 = total_spent.iloc[2,0]
total_purchase_values_4 = total_spent.iloc[3,0]
total_purchase_values_5 = total_spent.iloc[4,0]
top_purchase_values = [total_spent.iloc[0,0], total_spent.iloc[1,0], total_spent.iloc[2,0], total_spent.iloc[3,0],
                      total_spent.iloc[4,0]]

# Purchase Counts
top_purchase_counts_1 = df3[df3["SN"] == names[0]].count()[0]
top_purchase_counts_2 = df3[df3["SN"] == names[1]].count()[0]
top_purchase_counts_3 = df3[df3["SN"] == names[2]].count()[0]
top_purchase_counts_4 = df3[df3["SN"] == names[3]].count()[0]
top_purchase_counts_5 = df3[df3["SN"] == names[4]].count()[0]
top_purchase_counts = [top_purchase_counts_1, top_purchase_counts_2, top_purchase_counts_3, top_purchase_counts_4,
                       top_purchase_counts_5]

# Average Purchas Prices
avg_price_1 = total_purchase_values_1/top_purchase_counts_1
avg_price_2 = total_purchase_values_2/top_purchase_counts_2
avg_price_3 = total_purchase_values_3/top_purchase_counts_3
avg_price_4 = total_purchase_values_4/top_purchase_counts_4
avg_price_5 = total_purchase_values_5/top_purchase_counts_5
avg_prices = [avg_price_1, avg_price_2, avg_price_3, avg_price_4, avg_price_5]

# Dictionary of values
top_spenders_dict = {
    "Purchase Count": top_purchase_counts,
    "Average Purchase Price": avg_prices,
    "Total Purchase Value": top_purchase_values,
    "SN": top_names
}

# Creating DataFrame & setting index
top_spenders_df = pd.DataFrame(top_spenders_dict)
top_spenders_df = top_spenders_df.set_index("SN")
top_spenders_df = top_spenders_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]

# Formatting prices
top_spenders_df.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020" class="row_heading level0 row0" >Undirrala66</th> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row0_col0" class="data row0 col0" >5</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row0_col1" class="data row0 col1" >$3.41</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row0_col2" class="data row0 col2" >$17.06</td> 
    </tr>    <tr> 
        <th id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020" class="row_heading level0 row1" >Saedue76</th> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row1_col0" class="data row1 col0" >4</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row1_col1" class="data row1 col1" >$3.39</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row1_col2" class="data row1 col2" >$13.56</td> 
    </tr>    <tr> 
        <th id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020" class="row_heading level0 row2" >Mindimnya67</th> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row2_col0" class="data row2 col0" >4</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row2_col1" class="data row2 col1" >$3.18</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row2_col2" class="data row2 col2" >$12.74</td> 
    </tr>    <tr> 
        <th id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020" class="row_heading level0 row3" >Haellysu29</th> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row3_col0" class="data row3 col0" >3</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row3_col1" class="data row3 col1" >$4.24</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row3_col2" class="data row3 col2" >$12.73</td> 
    </tr>    <tr> 
        <th id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020" class="row_heading level0 row4" >Eoda93</th> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row4_col0" class="data row4 col0" >3</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row4_col1" class="data row4 col1" >$3.86</td> 
        <td id="T_5c8db16c_8e98_11e7_bc61_3c9509b4d020row4_col2" class="data row4 col2" >$11.58</td> 
    </tr></tbody> 
</table> 



# Most Popular Items


```python
df4 = df[["Item ID", "Item Name", "Price"]]
pop_items = df4.groupby("Item ID").count()
pop_items.sort_values(by = "Item Name", ascending = False, inplace = True)
df4 = df4.drop_duplicates(["Item ID", "Item Name"])

# Item IDs
item_ids = [pop_items.index[0], pop_items.index[1], pop_items.index[2], pop_items.index[3], pop_items.index[4]]

# Item Names
name_1 = df4.loc[df4["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = df4.loc[df4["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = df4.loc[df4["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = df4.loc[df4["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = df4.loc[df4["Item ID"] == item_ids[4], "Item Name"].item()
pop_item_names = [name_1, name_2, name_3, name_4, name_5]

# Purchase Counts
item_counts = [pop_items.iloc[0,0], pop_items.iloc[1,0], pop_items.iloc[2,0], pop_items.iloc[3,0], pop_items.iloc[4,0]]

# Item Prices
price_1 = df4.loc[df4["Item Name"] == pop_item_names[0], "Price"].item()
price_2 = df4.loc[df4["Item Name"] == pop_item_names[1], "Price"].item()
price_3 = df4.loc[df4["Item Name"] == pop_item_names[2], "Price"].item()
price_4 = df4.loc[df4["Item Name"] == pop_item_names[3], "Price"].item()
price_5 = df4.loc[df4["Item Name"] == pop_item_names[4], "Price"].item()
item_prices = [price_1,price_2,price_3,price_4,price_5]

# Total Purchase Value
total_values = [pop_items.iloc[0,0]*price_1, pop_items.iloc[1,0]*price_2, pop_items.iloc[2,0]*price_3, 
                pop_items.iloc[3,0]*price_4, pop_items.iloc[4,0]*price_5]

# Creating DataFrame & setting index
pop_items_df = pd.DataFrame({
    "Item ID": item_ids,
    "Item Name": pop_item_names,
    "Purchase Count": item_counts,
    "Item Price": item_prices,
    "Total Purchase Value": total_values
})
pop_items_df = pop_items_df.set_index(["Item ID", "Item Name"])
pop_items_df = pop_items_df[["Purchase Count", "Item Price", "Total Purchase Value"]]

# Formatting Prices
pop_items_df.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="index_name level1" >Item Name</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level0 row0" >39</th> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level1 row0" >Betrayal, Whisper of Grieving Widows</th> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row0_col0" class="data row0 col0" >11</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row0_col1" class="data row0 col1" >$2.35</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row0_col2" class="data row0 col2" >$25.85</td> 
    </tr>    <tr> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level0 row1" >84</th> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level1 row1" >Arcane Gem</th> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row1_col0" class="data row1 col0" >11</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row1_col1" class="data row1 col1" >$2.23</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row1_col2" class="data row1 col2" >$24.53</td> 
    </tr>    <tr> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level0 row2" >31</th> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level1 row2" >Trickster</th> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row2_col0" class="data row2 col0" >9</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row2_col1" class="data row2 col1" >$2.07</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row2_col2" class="data row2 col2" >$18.63</td> 
    </tr>    <tr> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level0 row3" >175</th> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level1 row3" >Woeful Adamantite Claymore</th> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row3_col0" class="data row3 col0" >9</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row3_col1" class="data row3 col1" >$1.24</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row3_col2" class="data row3 col2" >$11.16</td> 
    </tr>    <tr> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level0 row4" >13</th> 
        <th id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020" class="row_heading level1 row4" >Serenity</th> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row4_col0" class="data row4 col0" >9</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row4_col1" class="data row4 col1" >$1.49</td> 
        <td id="T_5ca4e068_8e98_11e7_b54f_3c9509b4d020row4_col2" class="data row4 col2" >$13.41</td> 
    </tr></tbody> 
</table> 



# Most Profitable Items


```python
df4 = df[["Item ID", "Item Name", "Price"]]
profit_items = df4.groupby("Item ID").sum()
profit_items.sort_values(by = "Price", ascending = False, inplace = True)
df4 = df4.drop_duplicates(["Item ID", "Price"])

# Item IDs
item_ids = [profit_items.index[0], profit_items.index[1], profit_items.index[2], profit_items.index[3], profit_items.index[4]]

# Item Names
name_1 = df4.loc[df4["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = df4.loc[df4["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = df4.loc[df4["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = df4.loc[df4["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = df4.loc[df4["Item ID"] == item_ids[4], "Item Name"].item()
profit_names = [name_1, name_2, name_3, name_4, name_5]

# Total Purchase Value
values = [profit_items.iloc[0,0],profit_items.iloc[1,0],profit_items.iloc[2,0],profit_items.iloc[3,0],profit_items.iloc[4,0]]

# Item Price
price_1 = df4.loc[df4["Item ID"] == item_ids[0], "Price"].item()
price_2 = df4.loc[df4["Item ID"] == item_ids[1], "Price"].item()
price_3 = df4.loc[df4["Item ID"] == item_ids[2], "Price"].item()
price_4 = df4.loc[df4["Item ID"] == item_ids[3], "Price"].item()
price_5 = df4.loc[df4["Item ID"] == item_ids[4], "Price"].item()
profit_prices = [price_1,price_2,price_3,price_4,price_5]

# Purchase counts
df5 = df[["Item ID", "Item Name", "Price"]].groupby("Item Name").count()
count_1 = df5.loc[df5.index == profit_names[0], "Item ID"].item()
count_2 = df5.loc[df5.index == profit_names[1], "Item ID"].item()
count_3 = df5.loc[df5.index == profit_names[2], "Item ID"].item()
count_4 = df5.loc[df5.index == profit_names[3], "Item ID"].item()
count_5 = df5.loc[df5.index == profit_names[4], "Item ID"].item()
counts = [count_1, count_2, count_3, count_4, count_5]

# Creating DataFrame & setting index
profit_items_df = pd.DataFrame({
    "Item ID": item_ids,
    "Item Name": profit_names,
    "Purchase Count": counts,
    "Item Price": profit_prices,
    "Total Purchase Value": values
})
profit_items_df = profit_items_df.set_index(["Item ID", "Item Name"])
profit_items_df = profit_items_df[["Purchase Count", "Item Price", "Total Purchase Value"]]

# Formatting prices
profit_items_df.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="index_name level1" >Item Name</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level0 row0" >34</th> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level1 row0" >Retribution Axe</th> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row0_col0" class="data row0 col0" >9</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row0_col1" class="data row0 col1" >$4.14</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row0_col2" class="data row0 col2" >$37.26</td> 
    </tr>    <tr> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level0 row1" >115</th> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level1 row1" >Spectral Diamond Doomblade</th> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row1_col0" class="data row1 col0" >7</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row1_col1" class="data row1 col1" >$4.25</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row1_col2" class="data row1 col2" >$29.75</td> 
    </tr>    <tr> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level0 row2" >32</th> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level1 row2" >Orenmir</th> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row2_col0" class="data row2 col0" >6</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row2_col1" class="data row2 col1" >$4.95</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row2_col2" class="data row2 col2" >$29.70</td> 
    </tr>    <tr> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level0 row3" >103</th> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level1 row3" >Singed Scalpel</th> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row3_col0" class="data row3 col0" >6</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row3_col1" class="data row3 col1" >$4.87</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row3_col2" class="data row3 col2" >$29.22</td> 
    </tr>    <tr> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level0 row4" >107</th> 
        <th id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020" class="row_heading level1 row4" >Splitter, Foe Of Subtlety</th> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row4_col0" class="data row4 col0" >8</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row4_col1" class="data row4 col1" >$3.61</td> 
        <td id="T_5cbd4bc8_8e98_11e7_8b9a_3c9509b4d020row4_col2" class="data row4 col2" >$28.88</td> 
    </tr></tbody> 
</table> 


