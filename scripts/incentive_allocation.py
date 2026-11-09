import pandas as pd
import numpy as np

def run_incentive_allocation(input_csv="data/bolt_driver_weekly_attendance_incentives-v2.csv"):
    df = pd.read_csv(input_csv)
    df['Calculated_Daily_Hours'] = df['Last_Week_Hours'] / 7.0

    def get_tier_label(h):
        if h < 3.0:
            return "Tier 1: <3h/day (Part-Time/Low)"
        elif 3.0 <= h < 6.0:
            return "Tier 2: 3-6h/day (Mid-Core/High Incentive)"
        elif 6.0 <= h < 8.0:
            return "Tier 3: 6-8h/day (High-Freq/Consolidation)"
        else:
            return "Tier 4: >=8h/day (Full-Time/Core)"

    def get_target_pct(h):
        if h < 3.0:
            return 0.0
        elif 3.0 <= h < 6.0:
            return 0.80
        elif 6.0 <= h < 8.0:
            return 0.40
        else:
            return 0.20

    df['Tier_Label'] = df['Calculated_Daily_Hours'].apply(get_tier_label)
    df['Target_Incentive_Rate'] = df['Calculated_Daily_Hours'].apply(get_target_pct)

    # Composite selection score: 60% Rating + 40% Hours
    df['Selection_Score'] = df['Rating'] * 0.6 + (df['Last_Week_Hours'] / df['Last_Week_Hours'].max()) * 0.4
    df['Tier_Rank'] = df.groupby('Tier_Label')['Selection_Score'].rank(ascending=False, method='first')
    df['Tier_Total'] = df.groupby('Tier_Label')['Driver_ID'].transform('count')
    df['Qualified_Quota'] = (df['Tier_Total'] * df['Target_Incentive_Rate']).round()
    df['Next_Week_Incentive_Eligible'] = df['Tier_Rank'] <= df['Qualified_Quota']
    df['Next_Week_Incentive_Eligible'] = df['Next_Week_Incentive_Eligible'].map({True: 'Yes', False: 'No'})

    bonus_map = {
        "Tier 1: <3h/day (Part-Time/Low)": 0.0,
        "Tier 2: 3-6h/day (Mid-Core/High Incentive)": 35.0,
        "Tier 3: 6-8h/day (High-Freq/Consolidation)": 50.0,
        "Tier 4: >=8h/day (Full-Time/Core)": 65.0
    }
    df['Proposed_Bonus_EUR'] = np.where(df['Next_Week_Incentive_Eligible'] == 'Yes', df['Tier_Label'].map(bonus_map), 0.0)
    return df

if __name__ == "__main__":
    result = run_incentive_allocation()
    print("Allocation completed successfully! Total winners:", (result['Next_Week_Incentive_Eligible'] == 'Yes').sum())
