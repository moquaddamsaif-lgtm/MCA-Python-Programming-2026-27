second=int(input("Enter time in second: "))
hours=second//3600
minute=(second %3600) // 60
remaining_second=second %60

print("Hours:", hours)
print("Minutes:", minute)
print("Seconds:", remaining_second)
