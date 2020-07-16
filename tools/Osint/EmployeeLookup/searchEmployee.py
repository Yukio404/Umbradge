from tools.Osint.EmployeeLookup.LinkedIn import searchLinkedIn
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def employee_lookup():
	company = input("Company: ")
	city = input("City: ")

	print("\n"+wait+"Searching For Employee Of '%s'...\n" % (company))

	linkedin = searchLinkedIn()
	linkedin.search(company, city)

	found = linkedin.found

	if found:
		employee = linkedin.employees

		TABLE_DATA = [
			("Num", "Name"),
		]

		x = 1
		for employe in employee:
			TABLE_DATA.append((x, employe))
			x += 1

		table = SingleTable(TABLE_DATA, title=" LinkedIn ")
		print(table.table)
