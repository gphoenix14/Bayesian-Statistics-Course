import tkinter as tk

##################################
# 1) Funzioni di calcolo
##################################

def parse_value(val):
    """
    Tenta di convertire la stringa val in un float.
    Restituisce None se 'X', vuoto o non interpretabile.
    """
    val = val.strip()
    if val.upper() == "X" or val == "":
        return None
    try:
        return float(val)
    except ValueError:
        return None

def complete_and_compute(table):
    """
    table: dizionario con le chiavi:
      - 'B_A'       : B ∩ A
      - 'B_notA'    : B ∩ ¬A
      - 'notB_A'    : ¬B ∩ A
      - 'notB_notA' : ¬B ∩ ¬A
      - 'sumB'      : somma riga B
      - 'sumnotB'   : somma riga ¬B
      - 'sumA'      : somma colonna A
      - 'sumnotA'   : somma colonna ¬A
      - 'sumTotal'  : somma totale (es. 100)

    Ogni valore può essere None (se l'utente ha messo 'X' o vuoto).
    
    Ritorna (tabella_completata, results):
       - tabella_completata: gli stessi campi, eventualmente completati.
       - results: dizionario con P(B∩A), P(B), P(A), P(A|B), ecc.
                  Vuoto se non si riescono a calcolare.
    """
    
    B_A       = parse_value(table.get('B_A'))
    B_notA    = parse_value(table.get('B_notA'))
    notB_A    = parse_value(table.get('notB_A'))
    notB_notA = parse_value(table.get('notB_notA'))
    
    sumB      = parse_value(table.get('sumB'))
    sumnotB   = parse_value(table.get('sumnotB'))
    sumA      = parse_value(table.get('sumA'))
    sumnotA   = parse_value(table.get('sumnotA'))
    sumTotal  = parse_value(table.get('sumTotal'))
    
    changed = True
    while changed:
        changed = False
        
        # 1) sumB = B_A + B_notA
        if sumB is not None:
            if B_A is not None and B_notA is None:
                B_notA = sumB - B_A
                changed = True
            elif B_notA is not None and B_A is None:
                B_A = sumB - B_notA
                changed = True
        
        # 2) sumnotB = notB_A + notB_notA
        if sumnotB is not None:
            if notB_A is not None and notB_notA is None:
                notB_notA = sumnotB - notB_A
                changed = True
            elif notB_notA is not None and notB_A is None:
                notB_A = sumnotB - notB_notA
                changed = True
        
        # 3) sumA = B_A + notB_A
        if sumA is not None:
            if B_A is not None and notB_A is None:
                notB_A = sumA - B_A
                changed = True
            elif notB_A is not None and B_A is None:
                B_A = sumA - notB_A
                changed = True
        
        # 4) sumnotA = B_notA + notB_notA
        if sumnotA is not None:
            if B_notA is not None and notB_notA is None:
                notB_notA = sumnotA - B_notA
                changed = True
            elif notB_notA is not None and B_notA is None:
                B_notA = sumnotA - notB_notA
                changed = True
        
        # Completamento delle somme se mancanti
        if sumB is None and (B_A is not None) and (B_notA is not None):
            sumB = B_A + B_notA
            changed = True
        if sumnotB is None and (notB_A is not None) and (notB_notA is not None):
            sumnotB = notB_A + notB_notA
            changed = True
        if sumA is None and (B_A is not None) and (notB_A is not None):
            sumA = B_A + notB_A
            changed = True
        if sumnotA is None and (B_notA is not None) and (notB_notA is not None):
            sumnotA = B_notA + notB_notA
            changed = True
        
        # sumTotal = sumB + sumnotB (oppure sumA + sumnotA)
        if sumTotal is None:
            if sumB is not None and sumnotB is not None:
                sumTotal = sumB + sumnotB
                changed = True
            elif sumA is not None and sumnotA is not None:
                sumTotal = sumA + sumnotA
                changed = True
        
        # Se sumTotal è noto, possiamo ancora completare
        if sumTotal is not None:
            if sumB is not None and sumnotB is None:
                sumnotB = sumTotal - sumB
                changed = True
            elif sumnotB is not None and sumB is None:
                sumB = sumTotal - sumnotB
                changed = True
            if sumA is not None and sumnotA is None:
                sumnotA = sumTotal - sumA
                changed = True
            elif sumnotA is not None and sumA is None:
                sumA = sumTotal - sumnotA
                changed = True
    
    # Mettiamo i valori (anche quelli completati) in un dizionario
    table_completed = {
        'B_A': B_A,
        'B_notA': B_notA,
        'notB_A': notB_A,
        'notB_notA': notB_notA,
        'sumB': sumB,
        'sumnotB': sumnotB,
        'sumA': sumA,
        'sumnotA': sumnotA,
        'sumTotal': sumTotal
    }
    
    # Calcolo delle probabilità
    results = {}
    if (sumTotal is not None and sumTotal > 0 and
        B_A is not None and B_notA is not None and
        notB_A is not None and notB_notA is not None):
        
        pBA        = B_A / sumTotal
        pBnotA     = B_notA / sumTotal
        pnotB_A    = notB_A / sumTotal
        pnotB_notA = notB_notA / sumTotal
        
        pB    = None
        pnotB = None
        pA    = None
        pnotA = None
        
        if sumB is not None:
            pB = sumB / sumTotal
        if sumnotB is not None:
            pnotB = sumnotB / sumTotal
        if sumA is not None:
            pA = sumA / sumTotal
        if sumnotA is not None:
            pnotA = sumnotA / sumTotal
        
        pA_given_B = None
        pB_given_A = None
        pA_given_notB = None
        pnotA_given_B = None
        pnotA_given_notB = None
        
        # P(A|B)
        if pB and pB != 0:
            pA_given_B = pBA / pB
            if pB != 0:
                pnotA_given_B = pBnotA / pB
        
        # P(B|A)
        if pA and pA != 0:
            pB_given_A = pBA / pA
        
        # P(A|¬B)
        if pnotB and pnotB != 0:
            pA_given_notB = pnotB_A / pnotB
            pnotA_given_notB = pnotB_notA / pnotB
        
        results = {
            'P(B∩A)': pBA,
            'P(B∩¬A)': pBnotA,
            'P(¬B∩A)': pnotB_A,
            'P(¬B∩¬A)': pnotB_notA,
            'P(B)': pB,
            'P(¬B)': pnotB,
            'P(A)': pA,
            'P(¬A)': pnotA,
            'P(A|B)': pA_given_B,
            'P(B|A)': pB_given_A,
            'P(A|¬B)': pA_given_notB,
            'P(¬A|B)': pnotA_given_B,
            'P(¬A|¬B)': pnotA_given_notB
        }
    
    return table_completed, results

##################################
# 2) Interfaccia Grafica (tkinter)
##################################

def calcola():
    """
    Legge i valori dalle Entry, esegue complete_and_compute,
    e mostra i risultati nella text box.
    """
    input_data = {
        'B_A': entry_B_A.get(),
        'B_notA': entry_B_notA.get(),
        'notB_A': entry_notB_A.get(),
        'notB_notA': entry_notB_notA.get(),
        'sumB': entry_sumB.get(),
        'sumnotB': entry_sumnotB.get(),
        'sumA': entry_sumA.get(),
        'sumnotA': entry_sumnotA.get(),
        'sumTotal': entry_sumTotal.get()
    }
    
    table_completed, results = complete_and_compute(input_data)
    
    # Puliamo la text box
    text_result.delete("1.0", tk.END)
    
    # Messaggio con la tabella completata
    text_result.insert(tk.END, "=== Tabella Completata ===\n")
    for k, v in table_completed.items():
        text_result.insert(tk.END, f"{k} = {v}\n")
    
    text_result.insert(tk.END, "\n=== Risultati Probabilità ===\n")
    if results:
        for k, v in results.items():
            if v is not None:
                text_result.insert(tk.END, f"{k}: {v:.4f}\n")
            else:
                text_result.insert(tk.END, f"{k}: impossibile calcolarlo\n")
    else:
        text_result.insert(tk.END, "Dati insufficienti o incoerenti per calcolare probabilità.\n")

def main():
    global entry_B_A, entry_B_notA, entry_notB_A, entry_notB_notA
    global entry_sumB, entry_sumnotB, entry_sumA, entry_sumnotA, entry_sumTotal
    global text_result
    
    root = tk.Tk()
    root.title("Conjoint Table - Compilazione e Calcolo")
    root.geometry("850x550")
    
    # Cornice in alto con le istruzioni
    frame_info = tk.Frame(root)
    frame_info.pack(pady=5)
    
    lbl_info = tk.Label(
        frame_info,
        text=(
            "Inserisci nelle celle i valori (frequenze o conteggi). "
            "Se vuoi che un valore venga calcolato automaticamente, "
            "inserisci 'X' o lascia il campo vuoto.\n\n"
            "Esempio di valori:\n"
            " - B∩A = 20, B∩¬A = 30, Somma(B) = 50, Somma(A) = 45, Totale = 100\n"
            " - Oppure puoi mettere X in Totale e fornire tutte le somme di riga e colonna.\n"
            "Poi premi 'Calcola' per completare la tabella e ottenere le probabilità."
        ),
        justify="left"
    )
    lbl_info.pack()
    
    # Frame per le entry in stile tabella
    frame_table = tk.Frame(root)
    frame_table.pack(pady=10)
    
    # Layout "tabellare"
    tk.Label(frame_table, text="").grid(row=0, column=0)
    tk.Label(frame_table, text="A").grid(row=0, column=1)
    tk.Label(frame_table, text="¬A").grid(row=0, column=2)
    tk.Label(frame_table, text="Somma (riga)").grid(row=0, column=3)
    
    tk.Label(frame_table, text="B").grid(row=1, column=0, padx=5)
    tk.Label(frame_table, text="¬B").grid(row=2, column=0, padx=5)
    tk.Label(frame_table, text="Somma (colonna)").grid(row=3, column=0)
    
    # Riga B
    entry_B_A = tk.Entry(frame_table, width=8)
    entry_B_A.grid(row=1, column=1, padx=5)
    entry_B_notA = tk.Entry(frame_table, width=8)
    entry_B_notA.grid(row=1, column=2, padx=5)
    entry_sumB = tk.Entry(frame_table, width=8)
    entry_sumB.grid(row=1, column=3, padx=5)
    
    # Riga ¬B
    entry_notB_A = tk.Entry(frame_table, width=8)
    entry_notB_A.grid(row=2, column=1, padx=5)
    entry_notB_notA = tk.Entry(frame_table, width=8)
    entry_notB_notA.grid(row=2, column=2, padx=5)
    entry_sumnotB = tk.Entry(frame_table, width=8)
    entry_sumnotB.grid(row=2, column=3, padx=5)
    
    # Riga Somma colonne
    entry_sumA = tk.Entry(frame_table, width=8)
    entry_sumA.grid(row=3, column=1, padx=5)
    entry_sumnotA = tk.Entry(frame_table, width=8)
    entry_sumnotA.grid(row=3, column=2, padx=5)
    entry_sumTotal = tk.Entry(frame_table, width=8)
    entry_sumTotal.grid(row=3, column=3, padx=5)
    
    # Bottone per calcolare
    btn_calc = tk.Button(root, text="Calcola", command=calcola)
    btn_calc.pack(pady=5)
    
    # Text box per i risultati
    text_result = tk.Text(root, width=100, height=15)
    text_result.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
