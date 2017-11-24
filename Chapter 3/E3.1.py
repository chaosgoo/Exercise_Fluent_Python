DIAL_CODES = [
    (86,'China'),
    (91,'India'),
    (1,'United States'),
    (62,'Indonesia'),
    (55,'Brazil'),
    (92,'Pakistan'),
    (880,'Bangladesh'),
    (234,'Nigeria'),
    (7,'Russia'),
    (81,'Japan'),
]

country_code = {country:code for code ,country in DIAL_CODES}
#键:值,此处country作为键,code 作为值
print(country_code)
code_counrty = {code:country.upper() for country,code in country_code.items() if code < 66}
print(code_counrty)
#code,counrty作为值,并将country统一转换成大写,过滤出code < 66 的内容