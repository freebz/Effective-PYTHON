def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


flow_per_second = flow_rate(weight_diff, time_diff, 1)
