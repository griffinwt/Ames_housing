    
    #set df equal to "home2", run it through this cleaning cycle, then return cleaned data

def sort_data(array):

    home2 = array.copy()    
    
    home2['ms_cat'] = 'other' #making a new column for zone categories
    home2.loc[(home2['ms_zoning'] == 'I (all)') | 
          (home2['ms_zoning'] == 'A (agr)') | 
          (home2['ms_zoning'] == 'C (all)'),
         'ms_cat']='ms1' #zone1 includes I, A, C types
    home2.loc[home2['ms_zoning'] == 'RH', 'ms_cat']='ms2'
    home2.loc[home2['ms_zoning'] == 'FV', 'ms_cat']='ms3'
    home2.loc[home2['ms_zoning'] == 'RM', 'ms_cat']='ms4'

    home2['n_cat'] = 7 #making a new column for neighborhood category- if there is anything my filters don't catch, they'll roll into "other"
    home2.loc[(home2['neighborhood'] == 'MeadowV') | (home2['neighborhood'] == 'IDOTRR'), 'n_cat']=0
    home2.loc[(home2['neighborhood'] == 'BRDale') | (home2['neighborhood'] == 'OldTown'), 'n_cat']=1
    home2.loc[(home2['neighborhood'] == 'Edwards') | (home2['neighborhood'] == 'BrkSide') | (home2['neighborhood'] == 'Sawyer'), 'n_cat']=2
    home2.loc[(home2['neighborhood'] == 'SWISU') | (home2['neighborhood'] == 'Landmrk') | (home2['neighborhood'] == 'Blueste'), 'n_cat']=3
    home2.loc[(home2['neighborhood'] == 'NAmes') | (home2['neighborhood'] == 'NPkVill'), 'n_cat']=4
    home2.loc[home2['neighborhood'] == 'Mitchell', 'n_cat']=5
    home2.loc[(home2['neighborhood'] == 'Gilbert') | (home2['neighborhood'] == 'SawyerW') | (home2['neighborhood'] == 'NWAmes'), 'n_cat']=6
    home2.loc[(home2['neighborhood'] == 'Timber') | (home2['neighborhood'] == 'Somerst'), 'n_cat']=8
    home2.loc[home2['neighborhood'] == 'ClearCr', 'n_cat']=9
    home2.loc[(home2['neighborhood'] == 'Veenker') | (home2['neighborhood'] == 'GrnHill'), 'n_cat']=10
    home2.loc[home2['neighborhood'] == 'NoRidge', 'n_cat']=11
    home2.loc[home2['neighborhood'] == 'NridgeHt', 'n_cat']=12
    home2.loc[home2['neighborhood'] == 'StoneBr', 'n_cat']=13 #neighborhoods ranked by price 1-14

    home2['h_cat'] = 1 #new column for heating categories
    home2.loc[home2['heating'] == 'GasA', 'h_cat']=2
    home2.loc[home2['heating'] == 'GasW', 'h_cat']=3 #grav/wall/other = 1, gasa = 2, gasw = 3

    home2['k_cat'] = 0 #new column for kitchen qual categories
    home2.loc[home2['kitchen_qual'] == 'TA', 'k_cat']=1
    home2.loc[home2['kitchen_qual'] == 'Gd', 'k_cat']=2
    home2.loc[home2['kitchen_qual'] == 'Ex', 'k_cat']=3 #fair/poor will be 1, TA will be 2, GD as 3, and EX as 4

    home2['st_cat'] = 'other' #new column for sale type categories
    home2.loc[home2['sale_type'] == 'New', 'st_cat']='New'
    home2.loc[(home2['sale_type'] == 'Oth') | (home2['sale_type'] == 'ConLI') | (home2['sale_type'] == 'ConLw'), 'st_cat']='occ'
    home2.loc[(home2['sale_type'] == 'CWD') | (home2['sale_type'] == 'Con'), 'st_cat']='cwn'
    home2.loc[(home2['sale_type'] == 'COD') | (home2['sale_type'] == 'ConLD'), 'st_cat']='cld' 

    home2['ex_cat'] = 1 #new column for exterior categories
    home2.loc[(home2['exter_cond'] == 'Fa') | (home2['exter_cond'] == 'Po'), 'ex_cat']=0
    home2.loc[(home2['exter_cond'] == 'Gd') | (home2['exter_cond'] == 'Ex'), 'ex_cat']=2 #ranked 1 for fa/po, 2 for TA, and 3 for gd/ex

    home2['hs_cat'] = 'other' #new column for house style categories
    home2.loc[(home2['house_style'] == 'SFoyer') | (home2['house_style'] == '1.5Unf'), 'hs_cat']='SF15U'
    home2.loc[(home2['house_style'] == '1.5Fin') | (home2['house_style'] == 'SLvl'), 'hs_cat']='15FSL'
    home2.loc[(home2['house_style'] == '2.5Unf') | (home2['house_style'] == '2.5Fin'), 'hs_cat']='25UF'

    home2['mas_cat'] = 'one' #new column for masonry type categories 
    home2.loc[(home2['mas_vnr_type'] == 'BrkFace') | (home2['mas_vnr_type'] == 'BrkCmn'), 'mas_cat']='two'
    home2.loc[home2['mas_vnr_type'] == 'Stone', 'mas_cat']='three' #make "none" = to 1, brick as 2, and stone as 3

    home2['cen_cat'] = 0
    home2.loc[home2['central_air'] == 'Y', 'cen_cat']=1 #makeing central air ordinal, since having it is clearly better than not

    home2['nz'] = home2['n_cat'] + home2['ms_cat'] #making a new column for neighborhood + zone

    #new features
    #home2['oqual_gla'] = home2['overall_qual']*home2['gr_liv_area']
    home2['garage'] = home2['garage_cars']*home2['garage_area']
    home2['liv_tot'] = home2['total_bsmt_sf']*home2['1st_flr_sf']*home2['gr_liv_area']
    home2['bedbath'] = (home2['half_bath'] + home2['full_bath']) / home2['bedroom_abvgr']

    array = home2.copy()

    return array #returns filtered df with new columns


def save_test(df, features_list, dum_cols):
    df = sort_data(df) #clean training data set
    X = df[features_list]
    #X['mas_vnr_area'].fillna(X['mas_vnr_area'].mean(), inplace=True) #filling in mean for this column's nans
    #X.fillna(0, inplace=True) #fill rest of numerical nans with 0
    #if dum_cols != 0: #if you need to get dummies in any categorical columns, it happens here, otherwise enter '0'
    # X.apply(lambda x: x.fillna(x.mean()), axis=0)
    X = pd.get_dummies(X, columns=dum_cols, drop_first=True)
    X = X._get_numeric_data().apply(lambda x: x.fillna(x.mean()), axis=0) #fill all nan numeric empty spots with the mean of that column
    X = X.fillna(0) #fill all other nans with 0
    print(X.shape)
    y = df['saleprice'].map(np.log) #add target
    lr = LinearRegression()
    lr.fit(X, y)
    print(f'Your R2 score is {lr.score(X, y)}') #print r2 score
    #print('first done')
    test = pd.read_csv('datasets/test.csv') #read in test file
    test.columns = [col.lower().replace(' ', '_') for col in test.columns] #reformat test columns
    sub = test[['id']].copy() #put id numbers in empty array

    test = sort_data(test) #run sorting function (above)
    print(test.shape)

    X_test = test[features_list] #create X value based on selected features
    X = X._get_numeric_data().apply(lambda x: x.fillna(x.mean()), axis=0) #fill all nan numeric empty spots with the mean of that column
    X = X.fillna(0) #fill all other nans with 0
    #X_test['mas_vnr_area'].fillna(X_test['mas_vnr_area'].mean(), inplace=True) #filling in mean for this column's nans
    # X_test.fillna(0, inplace=True) #fill rest of numerical nans with 0
    
    X_test = pd.get_dummies(X_test, columns=dum_cols, drop_first=True)
    print(X_test.shape)
    
    #X_test.fillna(0, inplace=True) #fill rest of numerical nans with 0
    #return X_test.isnull().sum()
    sub['SalePrice'] = lr.predict(X_test) #make new df column from predictions
    #print('sub done')
    sub['SalePrice'] = np.exp(sub['SalePrice'])
    sub = sub.rename(columns = {'id' : 'Id'}) #rename id column to fit submission model
    sub['Id'] = [int(n) for n in sub['Id']] #make id numbers ints to fit submission model
    print(sub.head())
    query = input('Save data? Please enter "yes" or "no".')
    if query == 'yes':
        sub.to_csv(f'models/{pd.Timestamp.now()}.csv', index=False) #save submission as new csv named after timestamp of creation
        return f"All done, submission {test_name} saved"
    elif query == 'no':
        return 'Better luck next time'



def make_model(df, features_list, dum_cols):
    df = sort_data(df) #clean training data set
    X = df[features] #will make nan (should only be numerical) values zeroes
    #X['mas_vnr_area'].fillna(df['mas_vnr_area'].mean(), inplace=True)
    #X.fillna(0, inplace=True)
    X = X._get_numeric_data().apply(lambda x: x.fillna(x.mean()), axis=0) #fill all nan numeric empty spots with the mean of that column
    X = X.fillna(0)
    if dum_cols != 0: #if you need to get dummies in any categorical columns, it happens here, otherwise enter '0'
        X = pd.get_dummies(X, columns=dum_cols, drop_first=True)
    y = df['saleprice'].map(np.log) #add target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2) #tt split - from lesson 3.04

    lr = LinearRegression() #this section for regular linear regression
    lr.fit(X_train, y_train)
    
    print(f'Your training score is {lr.score(X_train, y_train)}') #score training
    print(f'Your test score is {lr.score(X_test, y_test)}') #score test
    print(f'Your cross val scores are {cross_val_score(lr, X_train, y_train)}') #score
    print(f'Your mean cross val score is {cross_val_score(lr, X_train, y_train).mean()}') #mean of cross val score

    pred = lr.predict(X_test) #create preds
    
    residuals = np.exp(y_test) - np.exp(pred) #these are the residuals
    residuals.hist()
    plt.axvline(0, color = 'red')
    plt.show()
    return f'Your RMSE for test {pd.Timestamp.now()} is {metrics.mean_squared_error(y, pred)**.5}.' #print RMSE with timestamp



