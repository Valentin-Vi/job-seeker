import pandas as pd
import os

class Exporter:
  def __init__(self, out_dir):
    self.out_dir = out_dir or "./out/jobs.csv"

  def export_to_csv(self, jobsList):
    file_path = f"{self.out_dir}/jobs.csv"
    new_df = pd.DataFrame([job.as_dict() for job in jobsList])

    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        
        merged = new_df.merge(existing_df, how='left', indicator=True)
        unique_df = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])
        
        if not unique_df.empty:
            unique_df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_df.to_csv(file_path, index=False)
