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


# Premilinary data analysis

## 2. ncodpers
```
$ cat train_ver2.csv | cut -d , -f 2 | sort -d | uniq -c | wc -l
  956646
```

## 3. ind_empleado
```
$ cat train_ver2.csv | cut -d , -f 3 | sort -d | uniq -c   
27734
2492 A
3566 B
2523 F
13610977 N
  17 S
   1 "ind_empleado"  
```
## 4. pais_residencia
```
$ cat train_ver2.csv | cut -d , -f 4 | sort -d | uniq -c
27734  
 111 AD  
 221 AE  
  17 AL  
  68 AO  
4835 AR  
 476 AT  
 424 AU  
  34 BA  
1526 BE  
 476 BG  
   6 BM  
1514 BO  
2351 BR  
 102 BY  
  17 BZ  
 446 CA  
  17 CD  
  17 CF  
  34 CG  
1995 CH  
  51 CI  
 989 CL  
  85 CM  
 563 CN  
3526 CO  
 147 CR  
 758 CU  
 102 CZ  
4625 DE  
  11 DJ  
 226 DK  
 424 DO  
  86 DZ  
2169 EC  
  45 EE  
  68 EG  
13553710 ES  
  34 ET  
 345 FI  
5161 FR  
  51 GA  
4605 GB  
  17 GE  
  17 GH  
  17 GI  
  17 GM  
  51 GN  
 119 GQ  
 243 GR  
 130 GT  
  34 GW  
  51 HK  
 282 HN  
  68 HR  
  37 HU  
 409 IE  
 413 IL  
 187 IN  
  17 IS  
2947 IT  
  11 JM  
 239 JP  
  72 KE  
  17 KH  
  96 KR  
  17 KW  
  17 KZ  
  17 LB  
  45 LT  
 124 LU  
  17 LV  
  17 LY  
 396 MA  
  96 MD  
  51 MK  
  17 ML  
  17 MM  
  51 MR  
   2 MT  
2573 MX  
  34 MZ  
 214 NG  
  62 NI  
 757 NL  
 136 NO  
  51 NZ  
  22 OM  
  77 PA  
 900 PE  
  34 PH  
  85 PK  
 599 PL  
 101 PR  
1419 PT  
1430 PY  
  52 QA  
2931 RO  
  34 RS  
 769 RU  
  79 SA  
 603 SE  
 117 SG  
  85 SK  
  17 SL  
  68 SN  
 102 SV  
  17 TG  
 102 TH  
  17 TN  
  62 TR  
  34 TW  
 493 UA  
3651 US  
 510 UY  
2331 VE  
  34 VN  
 119 ZA  
  11 ZW  
   1 "pais_residencia"
```

## 5. sexo
```
$ cat train_ver2.csv | cut -d , -f 5 | sort -d | uniq -c
27804
6195253 H
7424252 V
   1 "sexo"
```

## 6. age
```
$ cat train_ver2.csv | cut -d , -f 6 | sort -d | uniq -c
 733   2
1534   3
2210   4
3004   5
3673   6
3792   7
4744   8
5887   9
7950  10
10481  11
12546  12
12745  13
12667  14
13118  15
11759  16
11953  17
10989  18
21597  19
422867  20
675988  21
736314  22
779884  23
734785  24
472016  25
347778  26
281981  27
240192  28
205709  29
186040  30
167985  31
169537  32
170477  33
174574  34
183577  35
198422  36
212420  37
231963  38
260548  39
287754  40
309051  41
319713  42
324303  43
322955  44
314771  45
299365  46
286505  47
271576  48
250484  49
236383  50
223297  51
211611  52
202527  53
181511  54
165355  55
151340  56
144645  57
134739  58
124177  59
117834  60
108356  61
101186  62
91521  63
87398  64
84750  65
81343  66
77693  67
78361  68
77745  69
70192  70
66825  71
67664  72
64431  73
59086  74
50597  75
48997  76
49218  77
34358  78
35065  79
35773  80
38217  81
33938  82
31860  83
30124  84
27754  85
24956  86
23648  87
21718  88
19175  89
16863  90
15098  91
13492  92
11642  93
10085  94
8511  95
7480  96
5962  97
4622  98
3617  99
27734  NA
3050 100
2666 101
2335 102
2003 103
1350 104
1280 105
 899 106
 594 107
 456 108
 265 109
 261 110
 252 111
 188 112
 117 113
  22 114
  82 115
  63 116
  14 117
   3 126
   8 127
   8 163
   3 164
   1 "age"
```
## 8. ind_nuevo
```
$ cat train_ver2.csv | cut -d , -f 8 | sort -d | uniq -c
12808368  0
811207  1
27734 NA
   1 "ind_nuevo"
```

## 10. indrel
```
$ cat train_ver2.csv | cut -d , -f 10 | sort -d | uniq -c
13594782  1
24793 99
27734 NA
   1 "indrel"
```

## 12. indrel_1mes
```
$ cat train_ver2.csv | cut -d , -f 12 | sort -d | uniq -c
149781
4357298 1
9133383 1.0
 577 2
 740 2.0
1570 3
2780 3.0
  83 4
 223 4.0
 874 P
   1 "indrel_1mes"
```

## 13. tiprel_1mes
```
$ cat train_ver2.csv | cut -d , -f 13 | sort -d | uniq -c
149781
6187123 A
7304875 I
   4 N
4656 P
 870 R
   1 "tiprel_1mes"
```

## 14. indresi
```
$ cat train_ver2.csv | cut -d , -f 14 | sort -d | uniq -c
27734
65864 N
13553711 S
   1 "indresi"
```

## 15. indext
```
$ cat train_ver2.csv | cut -d , -f 15 | sort -d | uniq -c
27734
12974839 N
644736 S
   1 "indext"
```

## 16. conyuemp
```
$ cat train_ver2.csv | cut -d , -f 16 | sort -d | uniq -c
13645501
1791 N
  17 S
   1 "conyuemp"
```

## 17. canal_entrada
```
$ cat train_ver2.csv | cut -d , -f 17 | sort -d | uniq -c
186126
 210 004
29063 007
27139 013
  11 025
 152 K00
66656 KAA
62381 KAB
7697 KAC
10680 KAD
50764 KAE
30559 KAF
74295 KAG
24875 KAH
37699 KAI
24280 KAJ
 838 KAK
7573 KAL
11285 KAM
1370 KAN
6676 KAO
14928 KAP
18017 KAQ
32686 KAR
86221 KAS
3268209 KAT
 249 KAU
 107 KAV
34275 KAW
67350 KAY
32186 KAZ
1298 KBB
 241 KBD
 147 KBE
3760 KBF
1725 KBG
7197 KBH
 519 KBJ
 575 KBL
 555 KBM
  61 KBN
7380 KBO
  85 KBP
4179 KBQ
1875 KBR
 714 KBS
3127 KBU
 896 KBV
1130 KBW
 102 KBX
 642 KBY
46446 KBZ
1530 KCA
5187 KCB
49308 KCC
3276 KCD
 309 KCE
 420 KCF
5399 KCG
24098 KCH
26546 KCI
 215 KCJ
 957 KCK
4187 KCL
3251 KCM
1117 KCN
 179 KCO
 158 KCP
 198 KCQ
 196 KCR
 236 KCS
 105 KCT
1081 KCU
 229 KCV
  67 KCX
 379 KDA
  17 KDB
1531 KDC
 534 KDD
 828 KDE
 726 KDF
 469 KDG
 191 KDH
  17 KDI
  11 KDL
2468 KDM
 197 KDN
1763 KDO
1001 KDP
1112 KDQ
8050 KDR
1924 KDS
1299 KDT
2588 KDU
 427 KDV
 772 KDW
1728 KDX
1960 KDY
 531 KDZ
 851 KEA
 370 KEB
 231 KEC
3011 KED
 175 KEE
 329 KEF
1895 KEG
1546 KEH
 944 KEI
9247 KEJ
 542 KEK
2483 KEL
  68 KEM
4917 KEN
 850 KEO
 146 KEQ
5904 KES
 265 KEU
 844 KEV
5687 KEW
35146 KEY
2433 KEZ
409669 KFA
 107 KFB
3098360 KFC
44461 KFD
 250 KFE
5529 KFF
6800 KFG
2579 KFH
 881 KFI
6620 KFJ
3913 KFK
3806 KFL
 371 KFM
4520 KFN
9487 KFP
 371 KFR
6694 KFS
8036 KFT
4914 KFU
  67 KFV
  28 KGC
  17 KGN
  28 KGU
8950 KGV
 989 KGW
9474 KGX
4138 KGY
  51 KHA
16418 KHC
116891 KHD
4055270 KHE
20674 KHF
241084 KHK
45128 KHL
183924 KHM
116608 KHN
8992 KHO
 691 KHP
591039 KHQ
   1 KHR
   5 KHS
75607 RED
   1 "canal_entrada"
```

## 18. indfall
```
$ cat train_ver2.csv | cut -d , -f 18 | sort -d | uniq -c
27734
13584813 N
34762 S
   1 "indfall"
```

## 22. ind_actividad_cliente
```
$ cat train_ver2.csv | cut -d , -f 22 | sort -d | uniq -c
6903158  0
5841260  1
429322  A"
124933  ILLES"
85202  LA"
235700  LAS"
27734 NA
   1 "ind_actividad_cliente"
```

## 24. segmento
```
$ cat train_ver2.csv | cut -d , -f 24 | sort -d | uniq -c | head -100
418613
545352 01 - TOP
7542889 02 - PARTICULARES
4506805 03 - UNIVERSITARIO
  17 100000.44
  17 100001.85
  11 100007.28
  17 100010.67
  17 100013.34
  17 100013.7
  17 100014.21
```

# Product stats

```
0    13645913
1        1396
Name: ind_ahor_fin_ult1, dtype: int64
0    13646993
1         316
Name: ind_aval_fin_ult1, dtype: int64
1    8945588
0    4701721
Name: ind_cco_fin_ult1, dtype: int64
0    13641933
1        5376
Name: ind_cder_fin_ult1, dtype: int64
0    12543689
1     1103620
Name: ind_cno_fin_ult1, dtype: int64
0    13518012
1      129297
Name: ind_ctju_fin_ult1, dtype: int64
0    13514567
1      132742
Name: ind_ctma_fin_ult1, dtype: int64
0    11886693
1     1760616
Name: ind_ctop_fin_ult1, dtype: int64
0    13056301
1      591008
Name: ind_ctpp_fin_ult1, dtype: int64
0    13623034
1       24275
Name: ind_deco_fin_ult1, dtype: int64
0    13624641
1       22668
Name: ind_deme_fin_ult1, dtype: int64
0    13060928
1      586381
Name: ind_dela_fin_ult1, dtype: int64
0    12518082
1     1129227
Name: ind_ecue_fin_ult1, dtype: int64
0    13395025
1      252284
Name: ind_fond_fin_ult1, dtype: int64
0    13566973
1       80336
Name: ind_hip_fin_ult1, dtype: int64
0    13522150
1      125159
Name: ind_plan_fin_ult1, dtype: int64
0    13611452
1       35857
Name: ind_pres_fin_ult1, dtype: int64
0    12930329
1      716980
Name: ind_reca_fin_ult1, dtype: int64
0    13041523
1      605786
Name: ind_tjcr_fin_ult1, dtype: int64
0    13297834
1      349475
Name: ind_valo_fin_ult1, dtype: int64
0    13594798
1       52511
Name: ind_viv_fin_ult1, dtype: int64
0.0    12885285
1.0      745961
Name: ind_nomina_ult1, dtype: int64
0.0    12821161
1.0      810085
Name: ind_nom_pens_ult1, dtype: int64
0    11901597
1     1745712
Name: ind_recibo_ult1, dtype: int64
```