scrollbar = tk.Scrollbar(self.textarea)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
self.textarea.config(yscrollcommand=scrollbar.set)# Notepad
