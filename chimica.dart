import 'dart:core';
import 'dart:io';
import 'dart:math';
class Elemento{
  int id;
  String name;
  String sym;
  double mass;
  int pedice=1;

  Elemento(this.id,this.name,this.sym,this.mass);//Costruttore
  
  printall(){
    print("${this.id}");
    print("${this.name}");
    print("${this.sym}");
    print("${this.mass}");
    print("${this.pedice}");

  }
}

List<Elemento> nelComposto=[];
List<Elemento> elementi=[];
Map<String,String> id_sym={};


isUpper(String x)
{
  if(x.toUpperCase()==x) 
    return true;
  else
    return false;
  
}

bool isNumeric(String x)
{
  if(x==null)
    return false;
  else
    return double.tryParse(x) != null; //TRYPARSE PROVA A FARE IL PARSE
}

findComposti(String formula){
  int lastparentesistart;
  int lastparentestiend;
  String lastEntry;
  for(int x=0;x<=formula.length-1;x++)
  { 
    if(!isNumeric(formula[x])){
    if(formula[x]!="("){
      if(x!=formula.length-1){
        if(isUpper(formula[x]))
          if(!isUpper(formula[x+1])){lastEntry=formula.substring(x,x+2);addElement(formula.substring(x,x+2)); x++;}
          else{lastEntry=formula[x];addElement(formula[x]);}
        else  print("Error");
      }
    else
      if(isUpper(formula[x])){lastEntry=formula[x];addElement(formula[x]);}
    }
    else{
      int y=x;
      lastparentesistart=x;
      while(formula[y]!=")")y++;
      findComposti(formula.substring(x+1,y));
      x=y;
      lastparentestiend=y;
    }

  }
  else
    {
      int psnumero=x;
      String daParsare;
      
      while(isNumeric(formula[psnumero])){
        if(psnumero==formula.length-1)break;
        psnumero++;
      }
      
      if ((x==psnumero)) {
        daParsare = formula[x];
      } 
      else {
        if(psnumero==formula.length-1)
          daParsare = formula.substring(x);
        else //ERROR HERE
        daParsare = formula.substring(x,psnumero);
      }//problema del substring che va in errore con index uguali
      
      if(formula[x-1]!=")")
        for(int tmp=1;tmp<=int.parse((daParsare))-1;tmp++)
          addElement(lastEntry);
      else
        for(int tmp=1;tmp<=int.parse(daParsare)-1;tmp++)
          findComposti(formula.substring(lastparentesistart+1,lastparentestiend));
      
      if(psnumero!=formula.length-1)
        x=psnumero-1;
      else
        x=psnumero; //Se non sei alla fine della formula x-1, per via del substrig
    }

  }

}
addElement(String x){
  bool trovato=false;
  int postrovato;
  int i=0;
  int id;

  nelComposto.forEach((f){
    if(f.sym==x){trovato = true;postrovato=i;}
    i++;
  });
  
  elementi.forEach((f){
    if(f.sym==x)id=f.id; //cerca la corrispomdenza tra id e sym
  });

  if(!trovato)
    nelComposto.add(Elemento(elementi[id].id, elementi[id].name, x, elementi[id].mass));
  
  else
    nelComposto[postrovato].pedice++;

}

double arrotonda(int decimali, double n){
  
  int fac=pow(10, decimali);

  return ((n*fac).round()/fac);

}

double calcolaMassa(){
  
  double massatot=0;
  int decimali=3;

  nelComposto.forEach((f){
    massatot+=f.mass*f.pedice;
  });
  
  return arrotonda(decimali, massatot);

}
void main(List<String> args) async {
  
  String formula = args.isNotEmpty ? args[0] :"H2O";
  String dataFile="Elementi.csv";
  File file = File(dataFile);
  
  elementi.add(Elemento(0, "name", "sym", 0));
  
  
  await file.readAsLines().then((x){
    x.forEach((f){
      var r=f.split(";");
      if(r[0]!="ID")
        elementi.add(Elemento(int.parse(r[0]), r[1], r[2], double.parse(r[3])));
    });
  });
  String formulacorr=formula+"()";
  findComposti(formulacorr);
  print("Massa Molare di ${formula} = ${calcolaMassa()} g/mol");
}

