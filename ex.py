from ContaBancaria import *
conta1 = ContaBancaria(3613136, 'lula', 'corrente')
conta1.AtivarConta()
conta1.Depositar(1000)
conta1.AjustaLimite(1000)
conta1.Sacar(1500)
conta1.VerificarSaldo()