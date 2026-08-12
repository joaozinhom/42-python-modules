file_name = "ancient_fragment.txt"
print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print(f"Accessing Storage Vault: {file_name}")

try:
    with open(file_name, 'r') as file:
        print("Connection established...\n")
        content = file.read()
        print("RECOVERED DATA:")
        print(content)
        print("\n\033[0;32m🟩 Data recovery complete. "
              "Storage unit disconnected.\033[0;37m")
except Exception:
    print("\033[0;31m🟥 ERROR: Storage vault not found.\033[0;37m")
