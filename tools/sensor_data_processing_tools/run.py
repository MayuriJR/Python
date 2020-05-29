from Tools.sensor_data_processing.filter.filter_data import DataFilter as df

src_path = r"C:\Users\Administrator\Desktop\BOut"
dest_path = src_path + "final"
dfr = df(src_path, dest_path)
dfr.run()
