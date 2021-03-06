import tkinter as tk
from tkinter import messagebox
import requests
import PIL

class GitHupUsuarioApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.URL_GITHUB = 'https://api.github.com/users/'

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('GitHub Usuarios Consulta')
        self.geometry('350x450')

        frm_entrada_datos = tk.Frame(self)
        frm_entrada_datos.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.9, anchor='n')

        self.txt_usuario = tk.Entry(frm_entrada_datos, font=('Arial', 13))
        self.txt_usuario.place(relx=0, rely=0, relheight=1, relwidth=0.65)

        btn_consultar = tk.Button(frm_entrada_datos, font=('Arial', 13), text='Consultar')
        btn_consultar.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)
        btn_consultar['command'] = self.consultar

        lbf_resultado = tk.LabelFrame(self, text='Resultados')
        lbf_resultado.place(relx=0.5, rely=0.25, relheight=0.9, relwidth=0.9, anchor='n')

        lbl_nombre = tk.Label(lbf_resultado, text='Nombre:', width=12, justify=tk.LEFT, anchor='w')
        lbl_nombre.grid(row=0, column=0, padx=10, pady=2)
        self.txt_nombre = tk.Entry(lbf_resultado, width=28)
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=2)
        
        lbl_fecha_creacion = tk.Label(lbf_resultado, text='Fecha creación:', width=12, justify=tk.LEFT, anchor='w')
        lbl_fecha_creacion.grid(row=1, column=0, padx=10, pady=2)
        self.txt_fecha_creacion = tk.Entry(lbf_resultado, width=28)
        self.txt_fecha_creacion.grid(row=1, column=1, padx=10, pady=2)
        
        lbl_url = tk.Label(lbf_resultado, text='URL:', width=12, justify=tk.LEFT, anchor='w')
        lbl_url.grid(row=2, column=0, padx=10, pady=2)
        self.txt_url = tk.Entry(lbf_resultado, width=28)
        self.txt_url.grid(row=2, column=1, padx=10, pady=2)
        
        lbl_gists = tk.Label(lbf_resultado, text='URL Gists:', width=12, justify=tk.LEFT, anchor='w')
        lbl_gists.grid(row=3, column=0, padx=10, pady=2)
        self.txt_gists = tk.Entry(lbf_resultado, width=28)
        self.txt_gists.grid(row=3, column=1, padx=10, pady=2)
        
        lbl_url_repos = tk.Label(lbf_resultado, text='URL repos:', width=12, justify=tk.LEFT, anchor='w')
        lbl_url_repos.grid(row=4, column=0, padx=10, pady=2)
        self.txt_url_repos = tk.Entry(lbf_resultado, width=28)
        self.txt_url_repos.grid(row=4, column=1, padx=10, pady=2)
        
        lbl_cantidad_repos = tk.Label(lbf_resultado, text='Cantidad repos:', width=12, justify=tk.LEFT, anchor='w')
        lbl_cantidad_repos.grid(row=5, column=0, padx=10, pady=2)
        self.txt_cantidad_repos = tk.Entry(lbf_resultado, width=28)
        self.txt_cantidad_repos.grid(row=5, column=1, padx=10, pady=2)
        
        lbl_ubicacion = tk.Label(lbf_resultado, text='Ubicación:', width=12, justify=tk.LEFT, anchor='w')
        lbl_ubicacion.grid(row=6, column=0, padx=10, pady=2)
        self.txt_ubicacion = tk.Entry(lbf_resultado, width=28)
        self.txt_ubicacion.grid(row=6, column=1, padx=10, pady=2)
        
        lbl_blog = tk.Label(lbf_resultado, text='Blog:', width=12, justify=tk.LEFT, anchor='w')
        lbl_blog.grid(row=7, column=0, padx=10, pady=2)
        self.txt_blog = tk.Entry(lbf_resultado, width=28)
        self.txt_blog.grid(row=7, column=1, padx=10, pady=2)

        lbl_foto = tk.Label(lbf_resultado, text='Foto:', width=12, justify=tk.LEFT, anchor='w')
        lbl_foto.grid(row=8, column=0, padx=10, pady=2)

    def consultar(self):
        nombre_usuario = self.txt_usuario.get().strip()

        if len(nombre_usuario) == 0:
            messagebox.showwarning('Mensaje', 'El campo Usuario es obligatorio.')
            return
        
        consulta = f'{self.URL_GITHUB}{nombre_usuario}'

        respuesta = requests.get(consulta)
        respuesta_json = respuesta.json()

        self.mostrar_datos(respuesta_json)
    
    def mostrar_datos(self, respuesta_json):
        try:
            self.txt_nombre.delete(0, 'end')
            self.txt_nombre.insert(0, respuesta_json['name'])
            self.txt_fecha_creacion.delete(0, 'end')
            self.txt_fecha_creacion.insert(0, respuesta_json['created_at'])
            self.txt_url.delete(0, 'end')
            self.txt_url.insert(0, respuesta_json['url'])
            self.txt_gists.delete(0, 'end')
            self.txt_gists.insert(0, respuesta_json['gists_url'])
            # TODO...
        except:
            messagebox.showwarning('Mensaje', 'El usuario especificado no existe en GitHub.')

def main():
    app = GitHupUsuarioApp()
    app.mainloop()

if __name__ == '__main__':
    main()
