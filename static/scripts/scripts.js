// Función para validar cajas de texto obligatorias del formulario
function validar(Arreglo){
  for(i=0;i<Arreglo.length;i++){
    valor = document.getElementById(Arreglo[i]).value;
    if( valor == null || valor.length == 0 || /^\s+$/.test(valor) ) {
      alert("El Campo " + Arreglo[i]+ " está vacío")
    }
   }
}


