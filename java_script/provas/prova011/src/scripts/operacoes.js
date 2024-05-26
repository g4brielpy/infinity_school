function sacar(valor, saldo) {
  if (valor > 0 && valor <= saldo) {
    saldo -= valor;
    return saldo;
  } else {
    throw "Saldo insuficiente ou valor inválido";
    // return saldo;
  }
}

function depositar(valor, saldo) {
  if (valor > 0) {
    saldo += Number(valor);
    return saldo;
  } else {
    throw "Valor inválido";
    // return saldo;
  }
}

export { sacar, depositar };
