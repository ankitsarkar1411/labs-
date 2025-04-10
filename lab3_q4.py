
filename = input("Enter the filename to sort: ")
output_filename = input("Enter the output filename: ")

with open(filename, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines if line.strip()]  
lines.sort(key=str.lower) 

with open(output_filename, 'w') as output_file:
    output_file.write("\n".join(lines))  

print(f"Sorted contents have been written to {output_filename}")
