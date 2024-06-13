import pandas as pd
import matplotlib.pyplot as plt

def plot_top_three_complaints(df):
    # Filter the DataFrame for the top three complaint types
    top_three_complaints = df['complaint_type'].value_counts().nlargest(3).index
    top_three_df = df[df['complaint_type'].isin(top_three_complaints)]

    # Group the filtered DataFrame by 'created_date' hour and 'complaint_type', and count occurrences
    hourly_complaint_counts = top_three_df.groupby([top_three_df['created_date'].dt.hour, 'complaint_type']).size().unstack(fill_value=0)

    # Calculate the total count of the top three complaint types for each hour
    total_counts_top_three = hourly_complaint_counts.sum(axis=1)

    # Calculate the percentage of each of the top three complaint types for each hour
    percentage_top_three = (hourly_complaint_counts.div(total_counts_top_three, axis=0) * 100)

    # Plotting
    plt.figure(figsize=(10, 6))
    for complaint_type in percentage_top_three.columns:
        plt.plot(percentage_top_three.index, percentage_top_three[complaint_type], label=complaint_type)

    plt.xlabel('Hour')
    plt.ylabel('Relative Proportion of Complaint Types (%)')
    plt.title('Relative Proportions of Top Three Complaint Types by Hour')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
#
