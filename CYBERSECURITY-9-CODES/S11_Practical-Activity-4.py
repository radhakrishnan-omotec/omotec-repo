# Sample: system components with dependencies
system_map = {
    "Email Gateway": ["DNS Server"],
    "DNS Server": ["ISP"],
    "CRM Software": ["Cloud Vendor", "Authentication Server"],
    "Authentication Server": ["Database"],
    "Database": []
}


def print_risk_chain(component, visited=None):
    if visited is None:
        visited = set()
    visited.add(component)

    for dependency in system_map.get(component, []):
        if dependency not in visited:
            print(f"{component} depends on {dependency}")
            print_risk_chain(dependency, visited)



# Visualize cascading risk from CRM Software
print("📉 Stacked Risk Chain from CRM Software:")
print_risk_chain("CRM Software")