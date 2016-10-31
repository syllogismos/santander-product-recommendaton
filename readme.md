# Santander

Under their current system, a small number of Santander’s customers receive many
recommendations while many others rarely see any resulting in an uneven customer
experience. In their second competition, Santander is challenging Kagglers to
predict which products their existing customers will use in the next month based
on their past behavior and that of similar customers.

With a more effective recommendation system in place, Santander can better meet
the individual needs of all customers and ensure their satisfaction no matter
where they are in life.

Based on Users history and previous products they subscribed to,
predict what products he will be interested in future.


# Data

In this competition, you are provided with 1.5 years of customers behavior data
from Santander bank to predict what new products customers will purchase.
The data starts at 2015-01-28 and has monthly records of products a customer has,
such as "credit card", "savings account", etc. You will predict what additional
products a customer will get in the last month, 2016-06-28, in addition to what
they already have at 2016-05-28. These products are the columns named: ind_(xyz)_ult1,
which are the columns #25 - #48 in the training data. You will predict what a
customer will buy in addition to what they already had at 2016-05-28. 

The test and train sets are split by time, and public and private leaderboard
sets are split randomly.


Id | Column Name |	Description
--- | --- | ---
1 | fecha_dato |	The table is partitioned for this column
2 | ncodpers |	Customer code
3 | ind_empleado |	Employee index: A active, B ex employed, F filial, N not employee, P pasive
4 | pais_residencia |	Customer's Country residence
5 | sexo |	Customer's sex
6 | age |	Age
7 | fecha_alta |	The date in which the customer became as the first holder of a contract in the bank
8 | ind_nuevo |	New customer Index. 1 if the customer registered in the last 6 months.
9 | antiguedad |	Customer seniority (in months)
10 | indrel |	1 (First/Primary), 99 (Primary customer during the month but not at the end of the month)
11 | ult_fec_cli_1t |	Last date as primary customer (if he isn't at the end of the month)
12 | indrel_1mes |	Customer type at the beginning of the month ,1 (First/Primary customer), 2 (co-owner ),P (Potential),3 (former primary), 4(former co-owner)
13 | tiprel_1mes |	Customer relation type at the beginning of the month, A (active), I (inactive), P (former customer),R (Potential)
14 | indresi |	Residence index (S (Yes) or N (No) if the residence country is the same than the bank country)
15 | indext |	Foreigner index (S (Yes) or N (No) if the customer's birth country is different than the bank country)
16 | conyuemp |	Spouse index. 1 if the customer is spouse of an employee
17 | canal_entrada |	channel used by the customer to join
18 | indfall |	Deceased index. N/S
19 | tipodom |	Addres type. 1, primary address
20 | cod_prov |	Province code (customer's address)
21 | nomprov |	Province name
22 | ind_actividad_cliente |	Activity index (1, active customer; 0, inactive customer)
23 | renta |	Gross income of the household
24 | segmento |	segmentation: 01 - VIP, 02 - Individuals 03 - college graduated
25 | ind_ahor_fin_ult1 |	Saving Account
26 | ind_aval_fin_ult1 |	Guarantees
27 | ind_cco_fin_ult1 |	Current Accounts
28 | ind_cder_fin_ult1 |	Derivada Account
29 | ind_cno_fin_ult1 |	Payroll Account
30 | ind_ctju_fin_ult1 |	Junior Account
31 | ind_ctma_fin_ult1 |	Más particular Account
32 | ind_ctop_fin_ult1 |	particular Account
33 | ind_ctpp_fin_ult1 |	particular Plus Account
34 | ind_deco_fin_ult1 |	Short-term deposits
35 | ind_deme_fin_ult1 |	Medium-term deposits
36 | ind_dela_fin_ult1 |	Long-term deposits
37 | ind_ecue_fin_ult1 |	e-account
38 | ind_fond_fin_ult1 |	Funds
39 | ind_hip_fin_ult1  |	Mortgage
40 | ind_plan_fin_ult1 |	Pensions
41 | ind_pres_fin_ult1 |	Loans
42 | ind_reca_fin_ult1 |	Taxes
43 | ind_tjcr_fin_ult1 |	Credit Card
44 | ind_valo_fin_ult1 |	Securities
45 | ind_viv_fin_ult1 |	Home Account
46 | ind_nomina_ult1 |	Payroll
47 | ind_nom_pens_ult1 |	Pensions
48 | ind_recibo_ult1 |	Direct Debit