def estimate_breach_cost(records_lost, downtime_hours, reputation_hit):
    base_cost = records_lost * 150  # $150 per record (average)
    downtime_cost = downtime_hours * 10000  # $10k per hour
    reputation_penalty = 0.2 if reputation_hit else 0.0
    total = base_cost + downtime_cost
    adjusted_total = total + (total * reputation_penalty)
    return round(adjusted_total, 2)




# Hypothetical breach scenario
records = 20000
downtime = 8
reputation_damaged = True


cost = estimate_breach_cost(records, downtime, reputation_damaged)

print(f"💸 Estimated Total Breach Cost: ${cost}")