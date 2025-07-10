import random

#Generating worker number
number_workers = 400

def workerGeneration(number_workers=400):
    firstname = ['Kunmi', 'Deji', 'Eyiwunmi', 'Oke', 'Somto', 'Stephen', 'Emeka', 'Joy']
    lastname = ['Ode', 'John', 'Olawore', 'Kenneth', 'Peter', 'Enua', 'Orji', 'Azu']
    gender = ['Male', 'Female']

    #set the. work array list
    workersarray = []

    for a in range(number_workers):
        worker = {
            'id': random.randint(1000, 9999),
            'fullname': f"{random.choice(firstname)} {random.choice(lastname)}",
            'gender': random.choice(gender),
            'salary': round(random.uniform(5000, 30000), 2)
        }
        workersarray.append(worker)
    return workersarray

#Generate Payment Slips
def generatePaymentSlips(workersarray):
    for worker in workersarray:
        try:
            level = "Unassigned"
            if 10000 < worker['salary'] < 20000:
                level = "A1"
            if 7500 < worker['salary'] < 30000 and worker['gender'] == 'Female':
                level = "A5-F"

            print(f"Payment Slip for {worker['fullname']} (ID: {worker['id']})")
            print(f"Gender: {worker['gender']}")
            print(f"Salary: ${worker['salary']}")
            print(f"Employee Level: {level}")
            print("="*40)
        except Exception as e:
            print(f"Error processing worker: {e}")

if __name__ == "__main__":
    workers = workerGeneration()
    generatePaymentSlips(workers)