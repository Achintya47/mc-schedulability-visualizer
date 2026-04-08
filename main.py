import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def plot_filtered_data(df, num_tasks, u_total, hi_ratio, cf):
    filtered_df = df.copy()

    # Apply filters only if not -1
    if num_tasks != -1:
        filtered_df = filtered_df[filtered_df['Num_Tasks'] == num_tasks]

    if u_total != -1:
        filtered_df = filtered_df[filtered_df['U_total'] == u_total]

    if hi_ratio != -1:
        filtered_df = filtered_df[filtered_df['HI_ratio'] == hi_ratio]

    if cf != -1:
        filtered_df = filtered_df[filtered_df['CF'] == cf]

    if filtered_df.empty:
        print("No data available for selected filters.")
        return

    filtered_df = filtered_df.sort_values(by='CF')

    plt.figure(figsize=(8, 5))

    plt.plot(filtered_df['CF'], filtered_df['TT_Merge_Schedulable_Count'],
             marker='o', label='TT-Merge')

    plt.plot(filtered_df['CF'], filtered_df['EDF_VD_Schedulable_Count'],
             marker='x', label='EDF-VD')

    plt.plot(filtered_df['CF'], filtered_df['IMC_PnG_Schedulable_Count'],
             marker='^', label='IMC-PnG')

    plt.plot(filtered_df['CF'], filtered_df['EDF_IMC_Schedulable_Count'],
             marker='s', label='EDF-IMC')

    plt.xlabel("Criticality Factor (CF)")
    plt.ylabel("Number of Successful Task Sets")
    plt.title("Schedulability vs CF")

    plt.legend()
    plt.grid(True)
    plt.show()


def create_gui(df):
    root = tk.Tk()
    root.title("Filter Selection")

    # Helper to get sorted unique values + "No Filter"
    def get_values(column):
        values = sorted(df[column].unique().tolist())
        return ["No Filter"] + values

    # Helper to convert dropdown value → backend value
    def parse_value(value, dtype=float):
        if value == "No Filter":
            return -1
        return dtype(value)

    # Dropdowns
    num_tasks_cb = ttk.Combobox(root, values=get_values('Num_Tasks'))
    num_tasks_cb.set("No Filter")

    u_total_cb = ttk.Combobox(root, values=get_values('U_total'))
    u_total_cb.set("No Filter")

    hi_ratio_cb = ttk.Combobox(root, values=get_values('HI_ratio'))
    hi_ratio_cb.set("No Filter")

    cf_cb = ttk.Combobox(root, values=get_values('CF'))
    cf_cb.set("No Filter")

    # Labels
    ttk.Label(root, text="Num_Tasks").grid(row=0, column=0)
    ttk.Label(root, text="U_total").grid(row=1, column=0)
    ttk.Label(root, text="HI_ratio").grid(row=2, column=0)
    ttk.Label(root, text="CF").grid(row=3, column=0)

    # Place dropdowns
    num_tasks_cb.grid(row=0, column=1)
    u_total_cb.grid(row=1, column=1)
    hi_ratio_cb.grid(row=2, column=1)
    cf_cb.grid(row=3, column=1)

    # Button action
    def on_submit():
        plot_filtered_data(
            df,
            parse_value(num_tasks_cb.get(), int),
            parse_value(u_total_cb.get(), float),
            parse_value(hi_ratio_cb.get(), float),
            parse_value(cf_cb.get(), float)
        )

    ttk.Button(root, text="Plot", command=on_submit).grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    
    df = pd.read_csv('TTMerge_EDFVD_IMCPNG_summary.csv')

    create_gui(df)