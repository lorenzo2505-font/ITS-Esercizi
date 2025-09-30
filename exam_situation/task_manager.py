import json

class TaskManager:
    def __init__(self, tasks: dict[str, dict[str, bool|str]] = {}) -> None:
        self.tasks: dict[str, dict[str, bool|str]] = tasks
    
    def create_task(self, task_id: str, descrizione: str) -> dict|str:

        if task_id in self.tasks:
            return 'Errore, la chiave esiste già'
        
        self.tasks[task_id] = {'descrizione': descrizione, 'completato': False}

        return self.tasks[task_id]
    
    def complete_task(self, task_id: str) -> dict|str:

        if task_id not in self.tasks:
            return 'Errore, la chiave non esiste'
        
        if self.tasks[task_id]['completato']:
            return 'la task è gà stata completata'
        
        self.tasks[task_id]['completato'] = True

        return self.tasks[task_id]
    
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict | str:
        
        if task_id not in self.tasks:
            return 'Errore, la chiave esiste'
        
        self.tasks[task_id]['descrizione'] = nuova_descrizione

        return self.tasks[task_id]
    
    def remove_task(self, task_id: str) -> dict | str:

        if task_id not in self.tasks:
            return 'task non presente'
        
        return self.tasks.pop(task_id)
    
    def list_tasks(self) -> list[str]:
        return list(self.tasks.keys())
    
    def get_task(self, task_id: str) -> dict | str:
        
        if task_id not in self.tasks:
            return 'task non presente'
        
        return self.tasks[task_id]



if __name__ == '__main__':

    with open('example.txt', 'r') as file:
        file.read()
    
    encoding: str = 'utf-8'
    PATH: str = 'info.json'

    with open(PATH, mode = 'r', encoding=encoding) as file:
        config: dict = json.load(file)
        print(config)
    
    with open(PATH, mode = "w") as file: # salva il dizionario come file json
        json.dump(config, file, indent = 4)


