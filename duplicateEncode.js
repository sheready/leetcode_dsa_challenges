function duplicateEncode(word){
    let result = "";
    const letters = word.toLowerCase();
    for(i in letters){
        let matched = false;
        for(j in letters){
            if(i !== j){
                if(letters[i] === letters[j]){
                    matched = true;
                    break;
                }
            }
        }
        if(matched === true){
            result += ")";
        }else{
            result += "(" ;
        }
    }
    return result;
 
  
}
console.log(duplicateEncode("(( @"));
