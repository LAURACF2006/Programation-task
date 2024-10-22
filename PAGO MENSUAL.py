def calcular_pago_mensual(principal, tasa_anual, plazo_anios):
    # Convertir la tasa de interés anual a una tasa mensual
    tasa_mensual = tasa_anual / 100 / 12
    # Calcular el número total de pagos mensuales
    total_meses = plazo_anios * 12
    
    # Calcular el pago mensual usando la fórmula
    pago_mensual = principal * (tasa_mensual * (1 + tasa_mensual) ** total_meses) / ((1 + tasa_mensual) ** total_meses - 1)
    
    return pago_mensual

# Detalles del préstamo
principal = 250000  # Principal del préstamo en euros
tasa_anual = 5      # Tasa de interés anual en porcentaje
plazo_anios = 30    # Plazo del préstamo en años

# Calcular el pago mensual
pago_mensual = calcular_pago_mensual(principal, tasa_anual, plazo_anios)

# Mostrar el resultado
print(f"El pago mensual para un préstamo de {principal}€ a una tasa anual de {tasa_anual}% durante {plazo_anios} años es: {pago_mensual:.2f}€")
