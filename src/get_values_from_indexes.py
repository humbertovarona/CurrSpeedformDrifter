def get_values_from_indexes(values, Indexes):
    if len(values) <= len(Indexes):
        raise ValueError("The Indexes vector must have a length less than the values vector")
    values_of_indices = [values[i] for i in Indexes]
    return values_of_indices
