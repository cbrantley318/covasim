import ctypes

# Load library
veclib = ctypes.CDLL('./libcovasim_interface.so')

# Define the CovaSimplifyResult struct
class CovaSimplifyResult(ctypes.Structure):
    _fields_ = [
        ("states_count", ctypes.c_uint16),
        ("num_exp", ctypes.POINTER(ctypes.c_uint16)),
        ("num_inf", ctypes.POINTER(ctypes.c_uint16)),
        ("num_symp", ctypes.POINTER(ctypes.c_uint16)),
        ("num_dead", ctypes.POINTER(ctypes.c_uint16)),
        ("num_severe", ctypes.POINTER(ctypes.c_uint16)),
        ("num_crit", ctypes.POINTER(ctypes.c_uint16)),
        ("num_recovered", ctypes.POINTER(ctypes.c_uint16)),
        ("new_exp", ctypes.POINTER(ctypes.c_uint16)),
        ("new_inf", ctypes.POINTER(ctypes.c_uint16)),
        ("new_symp", ctypes.POINTER(ctypes.c_uint16)),
        ("new_dead", ctypes.POINTER(ctypes.c_uint16)),
        ("new_severe", ctypes.POINTER(ctypes.c_uint16)),
        ("new_crit", ctypes.POINTER(ctypes.c_uint16)),
        ("new_recovered", ctypes.POINTER(ctypes.c_uint16))
    ]

# Define argument and return types
veclib.runCovaSimplify.argtypes = [ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16]
veclib.runCovaSimplify.restype = ctypes.POINTER(CovaSimplifyResult)

def run_simulation(N, connections_per_person, t, beta, new_beta_value, date_intervention, initial_infections):
    # Call the C function
    result_ptr = veclib.runCovaSimplify(N, connections_per_person, t, beta, new_beta_value, date_intervention, initial_infections)
    result = result_ptr.contents
    
    # Convert arrays to Python lists
    num_exp = [result.num_exp[i] for i in range(t)]
    num_inf = [result.num_inf[i] for i in range(t)]
    num_symp = [result.num_symp[i] for i in range(t)]
    num_dead = [result.num_dead[i] for i in range(t)]
    num_severe = [result.num_severe[i] for i in range(t)]
    num_crit = [result.num_crit[i] for i in range(t)]
    num_recovered = [result.num_recovered[i] for i in range(t)]
    new_exp = [result.new_exp[i] for i in range(t)]
    new_inf = [result.new_inf[i] for i in range(t)]
    new_symp = [result.new_symp[i] for i in range(t)]
    new_dead = [result.new_dead[i] for i in range(t)]

    new_severe = [result.new_severe[i] for i in range(t)]
    new_crit = [result.new_crit[i] for i in range(t)]
    new_recovered = [result.new_recovered[i] for i in range(t)]
    return {
        'states_count': result.states_count,
        'num_exp': num_exp,
        'num_inf': num_inf,
        'num_symp': num_symp,
        'num_dead': num_dead,
        'num_severe': num_severe,   
        'num_crit': num_crit,
        'num_recovered': num_recovered,
        'new_exp': new_exp,
        'new_inf': new_inf,
        'new_symp': new_symp,
        'new_dead': new_dead,
        'new_severe': new_severe,
        'new_crit': new_crit,
        'new_recovered': new_recovered
    }

# Example usage
if __name__ == "__main__":
    N = 100
    connections_per_person = 4
    t = 90
    beta = 0.016*1000*64
    new_beta_value = 0
    date_intervention = 0
    initial_infections = 10
    
    # print the results
    result = run_simulation(N, connections_per_person, t, beta, new_beta_value, date_intervention, initial_infections)
    print(f"States count: {result['states_count']}")
    print(f"Num exp array: {result['num_exp']}")
    print(f"Num inf array: {result['num_inf']}")
    print(f"Num symp array: {result['num_symp']}")
    print(f"Num dead array: {result['num_dead']}")
    print(f"Num severe array: {result['num_severe']}")
    print(f"Num crit array: {result['num_crit']}")
    print(f"Num recovered array: {result['num_recovered']}")
    print(f"New exp array: {result['new_exp']}")
    print(f"New inf array: {result['new_inf']}")
    print(f"New symp array: {result['new_symp']}")
    print(f"New dead array: {result['new_dead']}")
    print(f"New severe array: {result['new_severe']}")
    print(f"New crit array: {result['new_crit']}")
    print(f"New recovered array: {result['new_recovered']}")


