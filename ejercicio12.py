def obtener_tipo_mime(nombre_archivo):
    tipos_mime = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    
    if '.' in nombre_archivo:
        extension = nombre_archivo[nombre_archivo.rindex('.'):].lower() 
        if extension in tipos_mime:
            return tipos_mime[extension]
    return 'application/octet-stream'

nombre_archivo = input('Ingrese el nombre del archivo: ')

tipo_mime = obtener_tipo_mime(nombre_archivo)

print(f'Tipo MIME para "{nombre_archivo}": {tipo_mime}')
