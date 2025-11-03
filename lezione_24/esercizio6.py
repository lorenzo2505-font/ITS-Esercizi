def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:

    if conditionA or (conditionB and conditionC):
        return "Operazione permessa"
    
    return "Operazione negata"