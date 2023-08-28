countries_list = input().split(", ")
capitals_list = input().split(", ")
result = {countries_list[x]: capitals_list[x] for x in range(len(countries_list))}
for key, value in result.items():
    print(f"{key} -> {value}")

