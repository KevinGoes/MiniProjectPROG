label = tk.Label(text="Welkom bij de NS!", background='yellow', foreground='blue', width=50, height=3)
label.pack(side="top", fill="x", pady=10)
optie1 = tk.Button(text='Registreren', height=15, width=65, font=('Helvetica', 15, 'bold'),
                    background='royalblue',
                    foreground='white')
optie1.place(x=0, y=75)

optie2 = tk.Button(text='Stallen', height=15, width=65, font=('Helvetica', 15, 'bold'),
                    background='royalblue',
                    foreground='white',
                    highlightbackground="Black",
                    command=toonHome()
                   )
optie2.place(x=775, y=75)

optie3 = tk.Button(text='Ophalen', height=15, width=65, font=('Helvetica', 15, 'bold'),
                    background='royalblue',
                    foreground='white', highlightbackground="Black")
optie3.place(x=0, y=450)

optie4 = tk.Button(text='Informatie', height=15, width=65, font=('Helvetica', 15, 'bold'),
                    background='royalblue',
                    foreground='white', highlightbackground="Black")
optie4.place(x=775, y=450)