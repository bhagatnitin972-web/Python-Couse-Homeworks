length = float(input("Enter the length of the zander in centimeters: "))


legal_limit = 42


if length < legal_limit:
    shortage = legal_limit - length
    print(f"The zander is {shortage:.1f} cm below the legal size limit. Please release it back into the lake.")
else:
    print("The zander meets the size requirement. You can keep it!")