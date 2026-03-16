data = input("Enter the data packet: ")
reverse_data = data[::-1]

if data == reverse_data:
    print("Data Integrity Verified: Packet is unchanged.")
else:
    print("Warning: Data may be corrupted.")