class cuentaB:
    comision: float = 500
    
    def __init__(self, titular: str, saldo_ini: float, activo: bool):
        if saldo_ini < 0:
            raise ValueError("Su saldo inicnial no puede ser menor a cero")
        self.titular = titular
        self.saldo = saldo_ini
        self.activo = activo
        
    def mostrar_saldo(self) -> float:
        return self.saldo
    
    def desactivarCuenta(self) -> bool:
        self.activo = False
        return f"El estado de la cuenta es: {self.activo}"
    
    def activarCuenta(self) -> bool:
        self.activo = True
        return f"El estado de la cuenta es: {self.activo}"
    
    def depositar (self, monto: float):
        if monto >= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.saldo += monto
        return f"Se han depositado ${monto} y el saldo actual es de ${self.saldo}"
    
    def retirar (self, monto: float):
        if monto > self.saldo:
            raise ValueError("El monto es mayor al saldo actual")
        self.saldo -= monto
        return f"Se han retirado ${monto} y el saldo actual es de ${self.saldo}"
        