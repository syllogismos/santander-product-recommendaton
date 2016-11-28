"""
Author: Anil Karaka
Bayes Rawks
"""
from collections import Counter
import datetime
import gc
from operator import mul
from tqdm import tqdm
import pandas

# n = 24
# counters = [[Counter() for _ in range(n)] for i in range(n)]

PRODUCTS_COUNT = 24
HEADER = ["ncodpers", "ind_ahor_fin_ult1", "ind_aval_fin_ult1",
          "ind_cco_fin_ult1", "ind_cder_fin_ult1", "ind_cno_fin_ult1",
          "ind_ctju_fin_ult1", "ind_ctma_fin_ult1", "ind_ctop_fin_ult1",
          "ind_ctpp_fin_ult1", "ind_deco_fin_ult1", "ind_deme_fin_ult1",
          "ind_dela_fin_ult1", "ind_ecue_fin_ult1", "ind_fond_fin_ult1",
          "ind_hip_fin_ult1", "ind_plan_fin_ult1", "ind_pres_fin_ult1",
          "ind_reca_fin_ult1", "ind_tjcr_fin_ult1", "ind_valo_fin_ult1",
          "ind_viv_fin_ult1", "ind_nomina_ult1", "ind_nom_pens_ult1",
          "ind_recibo_ult1"]
BINARY_PROB_OFFSET = 1.0
COUNTER_OFFSET = 1.0


def update_counter(old, new, counters):
    """
    given older months product data and
    newer months product data update counter object
    old = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0]
    new = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0]

    counters[i][j] contains counter, c = {'00': m, '01': n, '11': o, '10': p}
    p({j = 1 on new} given {i = 1 on old}) = (c['11']*1.0)/(c['10'] + c['11'])
    p({j = 1 on new} given {i = 0 on old}) = (c['01']*1.0)/(c['00'] + c['01]))

    p({i = 1 on old} given {j = 1 on new}) = (c['11']*1.0)/(c['11'] + c['01'])
    p({i = 0 on old} given {j = 1 on new}) = (c['01']*1.0)/(c['11'] + c['01'])
    """
    products = len(old)
    for i in range(products):
        for j in range(products):
            # if old[j] == 1:
            #     # have this condition if a user subscribed to a product
            #     # in the older month.
            #     continue
            old_sub_value = int(old[i])
            new_sub_value = int(new[j])
            counter_key_name = str(old_sub_value) + str(new_sub_value)
            counters[i][j][counter_key_name] += 1

    return counters


def get_prob_matrix(counters):
    """
    prob0[i][j] contains P(i_old = 0/j_new = 1)
    prob1[i][j] contains P(i_old = 1/j_new = 1)
    """
    prob0 = [[0.0 for _ in range(PRODUCTS_COUNT)]
             for _ in range(PRODUCTS_COUNT)]
    prob1 = [[0.0 for _ in range(PRODUCTS_COUNT)]
             for _ in range(PRODUCTS_COUNT)]
    for i in range(PRODUCTS_COUNT):
        for j in range(PRODUCTS_COUNT):
            ij_dict = counters[i][j]
            prob0[i][j] = (ij_dict['11'] + COUNTER_OFFSET)/(ij_dict['11'] +
                                                            ij_dict['01'] +
                                                            2*COUNTER_OFFSET)
            prob1[i][j] = (ij_dict['01'] + COUNTER_OFFSET)/(ij_dict['11'] +
                                                            ij_dict['01'] +
                                                            2*COUNTER_OFFSET)
    return prob0, prob1


def str_from_date(date_time):
    """
    datetime object to 2016_04_28 string
    """
    return '_'.join(str(date_time.date()).split('-'))


def get_binary_prob_dist(new_tr):
    """
    given a dataframe, returns base prob of product subscription = 1
    for each product in the form of a list
    """
    no_of_entries = new_tr.shape[0]
    return [(sum(new_tr[x]) + BINARY_PROB_OFFSET)/no_of_entries for x in
            HEADER[1:]]


def get_counters_from_new_old_df(new_tr, old_tr):
    """
    given new and old data frames.. returns counters
    """
    counters = [[Counter() for _ in range(PRODUCTS_COUNT)]
                for _ in range(PRODUCTS_COUNT)]
    for i in tqdm(list(new_tr.index)):
        try:
            old = list(old_tr.loc[i])
            new = list(new_tr.loc[i])
            counters = update_counter(old, new, counters)
        except KeyError:
            pass
    return counters


def get_probability_dist(year, month, day):
    """
    given a date generate conditional probabilities of new subs given old subs

    year, month, date :: int

    returns a cond_prob0, cond_prob1, prob_sub
    cond_prob0[i][j] = p(old_sub_i = 0 given new_sub_j = 1)
    cond_prob1[i][j] = p(old_sub_i = 1 given new_sub_j = 1)
    prob_sub[i] = probability of new_sub_i = 1
    """

    new_tr, old_tr = get_new_old_dfs_from_month(month, year, day)

    counters = get_counters_from_new_old_df(new_tr, old_tr)
    prob_sub = get_binary_prob_dist(new_tr)

    del new_tr
    del old_tr
    gc.collect()

    prob0, prob1 = get_prob_matrix(counters)
    return (prob0, prob1, prob_sub)


def get_new_old_dfs_from_month(year, month, day):
    """
    given month, return new and old data frames from train data
    """
    if month == 1:
        old_month = 12
        old_year = year - 1
    else:
        old_month = month - 1
        old_year = year

    old_date_file = 'data/train_' + \
        str_from_date(datetime.datetime(old_year, old_month, day)) + '.csv'
    new_date_file = 'data/train_' + \
        str_from_date(datetime.datetime(year, month, day)) + '.csv'

    print "Loading probability new and old data sets"
    old_tr = pandas.read_csv(old_date_file, header=None, names=HEADER,
                             usecols=[1]+range(24, 48), index_col=0)
    new_tr = pandas.read_csv(new_date_file, header=None, names=HEADER,
                             usecols=[1]+range(24, 48), index_col=0)

    old_tr = old_tr.fillna(0)
    new_tr = new_tr.fillna(0)
    return new_tr, old_tr


def get_new_subs_from_prob_mat(subs, prob0, prob1, prob_sub):
    """
    old_subs: [0, 1, 1, 0] subs data
    prob0: conditional prob0
    prob1: conditional prob1
    prob_sub: base subs probabilities

    returns a string of subs in descending order of probs
    """
    prob_dict = {}
    products = HEADER[1:]
    for i, prod in enumerate(subs):
        if prod == 0:
            temp_list = []
            for j in range(PRODUCTS_COUNT):
                if subs[j] == 0:
                    temp_list.append(prob0[j][i])
                if subs[j] == 1:
                    temp_list.append(prob1[j][i])
            temp_list.append(prob_sub[i])
            prob_dict[products[i]] = reduce(mul, temp_list, 1.0)
    sorted_produts = sorted(prob_dict.items(),
                            cmp=lambda x, y: cmp(x[1], y[1]),
                            reverse=True)[:7]
    product_string = ' '.join([x[0] for x in sorted_produts])
    return product_string


def get_test_train_cv_names(year, month, day):
    """
    from the given month get the train, test and cv files names to load
    """
    if month == 1:
        old_year = year - 1
        old_month = 12
    else:
        old_year = year
        old_month = month - 1

    old_str = str_from_date(datetime.datetime(old_year, old_month, day))
    new_str = str_from_date(datetime.datetime(year, month, day))

    if new_str == "2016_06_28":
        test_file = 'data/test_ver2.csv'
        cv_file = None
    else:
        test_file = 'data/train_' + new_str + '.csv'
        cv_file = 'data/cv_' + new_str + '.csv'

    train_file = 'data/train_' + old_str + '.csv'
    return test_file, train_file, cv_file


def generate_submission(prob_tup, test_tup):
    """
    prob_tup: month data to generate prob distributions from
    test_tup: test month for which a submission to be generated
    """
    prob0, prob1, prob_sub = get_probability_dist(prob_tup[0],
                                                  prob_tup[1],
                                                  prob_tup[2])

    test_file, train_file, cv_file = get_test_train_cv_names(test_tup[0],
                                                             test_tup[1],
                                                             test_tup[2])
    test_data = pandas.read_csv(test_file, usecols=[1])
    test_data["added_products"] = [HEADER[1]]*test_data.shape[0]

    train_data = pandas.read_csv(train_file, header=None,
                                 names=HEADER, usecols=[1]+range(24, 48),
                                 index_col=0)
    for i in tqdm(test_data.index):
        person = test_data.loc[i]["ncodpers"]
        try:
            row = list(train_data.loc[person])
        except KeyError:
            row = [0]*PRODUCTS_COUNT
        added_products = get_new_subs_from_prob_mat(row, prob0, prob1,
                                                    prob_sub)
        test_data.set_value(i, "added_products", added_products)

    return test_data
