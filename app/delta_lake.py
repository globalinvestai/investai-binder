from deltalake import DeltaTable

dt = DeltaTable("./deltatbl-partitioned")
dt.files()
