length = float(input("Enter the length of the zander in centimeters: "))
LEGAL_LIMIT = 42
if length < LEGAL_LIMIT:
    shortfall = LEGAL_LIMIT - length
    print(f"The zander is {shortfall:.1f} cm below the legal size limit. Please release it back into the lake.")
else:
    print("The zander meets the size requirement. You can keep it.")