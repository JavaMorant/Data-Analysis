import pandas as pd
import unittest
from pathlib import Path
import time
from io import StringIO
import sys




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Python2.py <filename>")
        return
    df = readCsv(sys.argv[1])
    if (df is None):
        print("File is empty")
        return
    df = cleanData(df)
    writeCsv(df)
    substitution(df)
    descriptiveAnalysis(df)

def readCsv(fileName): #TODO Accept command line argument and use that as file name
    df = pd.read_csv(fileName) #TODO change file to args
    if (df.empty):
        print("File is empty")
        return None
    return df

def cleanData(df):
    # Drop all rows with NaN (empty) values
    df.dropna(inplace=True)

    # Drop all duplicate rows
    df.drop_duplicates(subset=['Record_Number'], keep='first', inplace=True)

    # Drop all rows that contain invalid values
    condition2 = df['RESIDENCE_TYPE'].isin(["P", "C"])
    condition3 = df['sex'].isin([1, 2]) 
    condition4 = df['age'].isin([1, 2, 3, 4, 5, 6, 7, 8])
    condition5 = df['Country_Of_Birth'].isin([1, 2])
    condition6 = df['Family_Composition'].isin(['0', '1', '2', '3', '4', '5', 'X'])
    condition7 = df['Marital_Status'].isin([1, 2, 3, 4, 5])
    condition8 = df['student'].isin([1, 2])
    condition9 = df['health'].isin([1, 2, 3, 4, 5, 6])
    condition10 = df['Ethnic_Group'].isin([1, 2, 3, 4, 5, 6])
    condition11 = df['Approximate_Social_Grade'].isin(['1', '2', '3', '4', 'X'])
    condition12 = df['Hours_Worked_Per_Week'].isin(['1','2', '3', '4', 'X'])
    condition13 = df['Region'].isin(['S92000003'])
    condition14 = df['religion'].isin([1, 2, 3, 4, 5, 6, 7, 8, 9])
    condition15 = df['Occupation'].isin(['1', '2', '3', '4', '5', '7','8', '9', 'X'])
    condition16 = df['industry'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'X'])
    
    # Create a boolean series
    booleanSeries = condition2 & condition3 & condition4 & condition5 & condition6 & condition7 & condition8 & condition9 & condition10 & condition11 & condition12 & condition13 & condition14 & condition15 & condition16

    # Filter out all rows that contain invalid values
    df = df[booleanSeries]


    # Return refined dataframe
    return df

# Writes dataframe to csv file
def writeCsv(df):
    df.to_csv('../data/New_Scotland_teaching_file_1PCT.csv', index=False)

def descriptiveAnalysis(df):
    # print number of rows
    print("Number of rows: ", df.shape[0])
    # prints all variables and their respective types
    # print(df.dtypes)

    #value counts for each variable
    for col in df.columns:
        #time.sleep(1)
        
        if (col != 'Record_Number') and (col != 'Region'):
            
            value_counts = df[col].value_counts()
            # print(f"\n{col}:")

            for index, value in value_counts.items():
                print(f"{index}: {value}\n") 
                # Save to file
                with open('../data/DescriptiveAnalysis.txt', 'a') as f:
                    for index, value in value_counts.items():
                        print(f"{index}: {value}")
                        # Write to 
                        f.write(f"{col}, {index}: {value}\n")
                    # Add an extra newline for better formatting in the output file
                    f.write("\n")

        

def substitution(df): # TODO needs corrected
    replacementDict = {
        'Region': {
            'S92000003': 'Scotland'
        },
        'RESIDENCE_TYPE': {
            'C': 'Resident in a Communal Establishment',
            'P': 'Not a resident in a Communal Establishment'
        }, 
        'Family_Composition': {
            '0': '0',
            '1': '1', 
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            'X': '6 or more'
        },
        'sex': {
            1: 'Male',
            2: 'Female'
        },
        'age': {
            1: '0 to 15',
            2: '16 to 24',
            3: '25 to 34',
            4: '35 to 44',
            5: '45 to 54',
            6: '55 to 64',
            7: '65 to 74',
            8: '75 and over'
        },
        'Marital_Status': {
            1: 'Married',
            2: 'Widowed',
            3: 'Divorced',
            4: 'Separated',
            5: 'Never married'
        },
        'student': { 
            1: 'Yes',
            2: 'No'
        }, 
        'Country_Of_Birth': {
            1: 'UK',
            2: 'Non-UK'
        },
        'health': {
            1: 'Very good',
            2: 'Good',
            3: 'Fair',
            4: 'Bad',
            5: 'Very bad'
        }, 
        'Ethnic_Group': {
            1: 'White',
            2: 'Mixed',
            3: 'Asian',
            4: 'Black',
            5: 'Chinese',
            6: 'Other'
        },
        'religion': {
            1: 'No religion',
            2: 'Christian',
            3: 'Buddhist',
            4: 'Hindu',
            5: 'Jewish',
            6: 'Muslim',
            7: 'Sikh',
            8: 'Other religion',
            9: 'Not stated'
        },
        'Economic_Activity': {
            '1': 'Economically active: employed',
            '2': 'Economically active: self-employed',
            '3': 'Economically inactive: looking after home/family',
            '4': 'Economically inactive: long-term sick or disabled',
            '5': 'Economically inactive: student',
            '6': 'Economically inactive: retired',
            '7': 'Economically inactive: other',
            '8': 'Economically active: unemployed',
            '9': 'Economically active: Full-time student',
            'X': 'Not known'
        },
        'Occupation': {
            '1': 'Managers, directors and senior officials',
            '2': 'Professional occupations',
            '3': 'Associate professional and technical occupations',
            '4': 'Administrative and secretarial occupations',
            '5': 'Skilled trades occupations',
            '6': 'Caring, leisure and other service occupations',
            '7': 'Sales and customer service occupations',
            '8': 'Process, plant and machine operatives',
            '9': 'Elementary occupations',
            'X': 'Not known'
        },
        'industry': {
            '1': 'Agriculture, forestry and fishing',
            '2': 'Mining and quarrying; Manufacturing; Electricity, gas, steam and air conditioning supply; Water supply',
            '3': 'Construction',
            '4': 'Wholesale and retail trade; repair of motor vehicles and motorcycles',
            '5': 'Accommodation and food service activities',
            '6': 'Transportation and storage; Information and communication',
            '7': 'Financial and insurance activities',
            '8': ' Real estate activities; professional, scientific and technical activities; Administrative and support service activities',
            '9': 'Public administration and defence',
            '10': 'Education',
            '11': 'Human health and social work activities',
            '12': 'Arts, entertainment and recreation',
            '13': 'Other'
        },
        'Hours_Worked_Per_Week': {
            '1': '0 to 15',
            '2': '16 to 30',
            '3': '31 to 45',
            '4': '46 to 60',
            'X': 'Not known'
        }, 
        'Approximate_Social_Grade': {
            '1': 'AB',
            '2': 'C1',
            '3': 'C2',
            '4': 'DE',
            'X': 'Not known'
        }
    }

    # Replace values
    df.replace(replacementDict, inplace=True)

    # Return dataframe
    return df

        

    

# # Run main function
# if __name__ == "__main__":
#    main()
#    print ("Done")

# Testing
# df['Record_Number'].is_unique # Returns true if unique,
# df['RESIDENCE_TYPE'].isin(['C', 'P'])


# class TestDataCleaning(unittest.TestCase):


#     def setUp(self):
#         self.df = pd.DataFrame({
#             'RESIDENCE_TYPE': ['C', 'P', np.nan],
#             'sex': [1, 2, 3],
#             'age': [1, 2, 9],
#             'Country_Of_Birth': [1, 2, 3],
#             'Family_Composition': ['0', 'X', 'A'],
#             'Marital_Status': [1, 2, 6],
#             'student': [1, 2, 3],
#             'health': [1, 6, 4],
#             'Ethnic_Group': [1, 2, 7],
#             'Approximate_Social_Grade': ['1', '4', '5'],
#             'Hours_Worked_Per_Week': ['X', '4', '3'],
#             'Region': ['S92000003', 'S12345678', 'S23456789'],
#             'religion': [1, 9, 10],
#             'Occupation': ['1', 'X', '5'],
#             'industry': ['12', '8', '14']
#         })

#     def test_drops_nan_rows(self):
#         df = self.df.copy()
#         df.iloc[2] = np.nan
#         cleaned_df = cleanData(df)
#         self.assertEqual(cleaned_df.shape, (2, 15))

#     def test_drops_duplicate_rows(self):
#         df = pd.concat([self.df, self.df])
#         cleaned_df = cleanData(df)
#         self.assertEqual(cleaned_df.shape, (15, 15))

#     def test_filters_out_invalid_values(self):
#         df = self.df.copy()
#         cleaned_df = cleanData(df)
#         self.assertEqual(cleaned_df.shape, (2, 15))
#         self.assertEqual(cleaned_df['RESIDENCE_TYPE'].tolist(), ['Resident in a Communal Establishment', 'Not a resident in a Communal Establishment'])
#         self.assertEqual(cleaned_df['sex'].tolist(), ['Male', 'Female'])
#         self.assertEqual(cleaned_df['age'].tolist(), ['0 to 15', '16 to 24'])
#         self.assertEqual(cleaned_df['Country_Of_Birth'].tolist(), ['UK', 'Non-UK'])
#         self.assertEqual(cleaned_df['Family_Composition'].tolist(), ['0', '6 or more'])
#         self.assertEqual(cleaned_df['Marital_Status'].tolist(), ['Married', 'Widowed'])
#         self.assertEqual(cleaned_df['student'].tolist(), ['Yes', 'No'])
#         self.assertEqual(cleaned_df['health'].tolist(), ['Very good', 'Bad'])
#         self.assertEqual(cleaned_df['Ethnic_Group'].tolist(), ['White', 'Mixed'])
#         self.assertEqual(cleaned_df['Approximate_Social_Grade'].tolist(), ['AB', 'DE'])
#         self.assertEqual(cleaned_df['Hours_Worked_Per_Week'].tolist(), ['Not known', '46 to 60'])
#         self.assertEqual(cleaned_df['Region'].tolist(), ['Scotland', 'S23456789'])
#         self.assertEqual(cleaned_df['religion'].tolist(), ['No religion', 'Not stated'])
#         self.assertEqual(cleaned_df['Occupation'].tolist(), ['Managers, directors and senior officials', 'Skilled trades occupations'])
#         self.assertEqual(cleaned_df['industry'].tolist(), ['Arts, entertainment and recreation', 'Other'])

#     def test_readCsv(self):
#         # Test if readCsv() returns None for an empty CSV file
#         assertThrows  #TODO (explain) Mock empty DataFrame
#         self.assertIsNone(readCsv(sys.argv[1])) # Test if readCsv() returns None for an empty CSV file

#     def test_cleanData(self):
#         data = StringIO("""Record_Number,RESIDENCE_TYPE,sex,age,Country_Of_Birth,Family_Composition,Marital_Status,student,health,Ethnic_Group,Approximate_Social_Grade,Hours_Worked_Per_Week,Region,religion
#                           1,P,1,1,1,0,5,2,1,1,1,1,S92000003,1
#                           1,P,1,1,1,0,5,2,1,1,1,1,S92000003,1
#                           2,P,2,2,2,3,3,1,2,2,2,2,S92000003,2
#                           3,C,1,8,1,0,1,2,5,1,4,4,S92000003,9
#                           4,P,2,6,2,5,2,1,3,6,3,3,S92000003,7""")
#         df = pd.read_csv(data, sep=',', header=0, index_col=0)
#         time.sleep(1)
#         print (df)
#         time.sleep(1)
#         cleaned_df = cleanData(df)

#         # Check if duplicates are removed
#         self.assertEqual(cleaned_df.shape[0], 3)
        
#         # Check if rows with invalid values are removed
#         self.assertTrue(cleaned_df["religion"].isin([1, 2, 3, 4, 5, 6, 7, 8, 9]).all())

#     def test_substitution(self):
#         data = StringIO("""Record_Number,RESIDENCE_TYPE,sex,age,Country_Of_Birth,Family_Composition,Marital_Status,student,health,Ethnic_Group,Approximate_Social_Grade,Hours_Worked_Per_Week,Region,religion
#                           1,P,1,1,1,0,5,2,1,1,1,1,S92000003,1
#                           2,P,2,2,2,3,3,1,2,2,2,2,S92000003,2
#                           3,C,1,8,1,0,1,2,5,1,4,4,S92000003,9""")
#         df = pd.read_csv(data)
#         substituted_df = substitution(df)

#         # Test if the substitutions are correct
#         self.assertEqual(substituted_df.loc[0, "RESIDENCE_TYPE"], "Not a resident in a Communal Establishment")
#         # self.assertEqual(substituted_df.loc[1, "sex"], "Female")
#         # self.assertEqual(substituted_df.loc[2, "age"], "75 and over")
#         # self.assertEqual(substituted_df.loc[0, "Region"], "Scotland")
#         # self.assertEqual(substituted_df.loc[2, "religion"], "Not stated")
#     # def test_writeCsv(self, mock_to_csv):
#     #     data = StringIO("""Record_Number,RESIDENCE_TYPE,sex,age,Country_Of_Birth,Family_Composition,Marital_Status,student,health,Ethnic_Group,Approximate_Social_Grade,Hours_Worked_Per_Week,Region,religion
#     #                     1,P,1,1,1,0,5,2,1,1,1,1,S92000003,1
#     #                     2,P,2,2,2,3,3,1,2,2,2,2,S92000003,2
#     #                     3,C,1,8,1,0,1,2,5,1,4,4,S92000003,9""")
#     #     df = pd.read_csv(data)
#     #     writeCsv(df)
#     #     mock_to_csv.assert_called_once()

#     # def test_descriptiveAnalysis(self, mock_print):
#     #     data = StringIO("""Record_Number,RESIDENCE_TYPE,sex,age,Country_Of_Birth,Family_Composition,Marital_Status,student,health,Ethnic_Group,Approximate_Social_Grade,Hours_Worked_Per_Week,Region,religion
#     #                       1,P,1,1,1,0,5,2,1,1,1,1,S92000003,1
#     #                       2,P,2,2,2,3,3,1,2,2,2,2,S92000003,2
#     #                       3,C,1,8,1,0,1,2,5,1,4,4,S92000003,9""")
#     #     df = pd.read_csv(data)
#     #     descriptiveAnalysis(df)
        
#     #     # Test if the print function is called with the expected number of rows
#     #     mock_print.assert_any_call("Number of rows: ", 3)

# if __name__ == '__main__':  
#     print("Running unit tests...")
#     time.sleep(1)
#     # Load test cases from TestDataCleaning
#     test_cases = unittest.TestLoader().loadTestsFromTestCase(TestDataCleaning)

#     # Create a test suite containing the test cases
#     suite = unittest.TestSuite([test_cases])

#     # Run the test suite
#     unittest.TextTestRunner(verbosity=2).run(suite)


