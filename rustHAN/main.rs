/*
 * HAN interpreter made in Rust!
 * This interpreter is very crude and tries to copy the pyHAN compiler logic.
 * This does not implement the experimental function features found in pyHAN yet.
 */

extern crate eval;

use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::process;
use std::collections::HashMap;
use std::convert::TryInto;
use eval::eval;

// Use variable name and floating point interchangeably
fn interpret(s: String,var: &mut HashMap<String, f64>) -> f64 {
    if &s[0..1] != "$" {
        return s.parse::<f64>().unwrap();
    }
    else {
        return *var.get(&s[1..]).unwrap();
    }
}

// Evaluate binary conditions
fn cond(l: &Vec<String>,var: &mut HashMap<String, f64>) -> bool{
    let statement = format!("{} {} {}",interpret(l[1].clone(),var).to_string(),l[2].clone(),interpret(l[3].clone(),var).to_string());
    return eval(&statement).unwrap().as_bool().unwrap();
}

fn main() {
    // Get file path and read file
    let args: Vec<String> = env::args().collect();
    if args.len() <= 1 {
        println!("Error please specify a file path.");
        process::exit(1);
    }
    let filename = String::from(&args[1]);

    // Open the file
    let file = File::open(&filename).unwrap();
    let reader = BufReader::new(file);
    let fname : Vec<&str>= filename.split("/").collect();
    println!("Running rustHAN {version}\nInterpreter for the HAN language https://github.com/ARYANTECH123/HAN\nReading {file}\n\n",version=env!("CARGO_PKG_VERSION"),file=fname[fname.len()-1]);
    
    // Symbol table for the program
    let mut var : HashMap<String, f64>= HashMap::new();

    // Processing and tokenizing program
    let mut bc : Vec<String> = Vec::new();
    let mut tk : Vec<Vec<String>> = Vec::new();

    // Read the file line by line and append tokens to tk
    for line in reader.lines() {
        let line = line.unwrap().to_string();
        let line = line.to_string().trim().to_string();
        if line == ""{
            continue;
        }
        let tokens: Vec<String> = line.split(" ").map(|s| s.to_string()).collect();
        let mut line_tokens: Vec<String> = Vec::new();
        for i in 0..tokens.len(){
            if tokens[i] != "" {
                line_tokens.push(tokens[i].to_string());
            }
        }
        bc.push(line);
        tk.push(line_tokens);
    }
    tk.push(vec!["end".to_string()]);

    // Counters used 
    let mut i = 0; // Instruction pointer

    loop {
        if i >= tk.len() {
            break;
        }
        let line = &tk[i];
        
        // General IO
        if line[0] == "pr" {
            if &line[1][0..1] == "$" {
                let varname = line[1][1..].to_string();
                println!("{:}",var.get(&varname[..]).unwrap());
            }
            else {
                println!("{:}",bc[i][3..].to_string());
            }
        }

        // Variable Handling
        else if line[0] == "set" || line[0] == "let" {
            let v = interpret(line[3].clone(),&mut var);
            var.insert(line[1].clone(),v);
        }

        // Integer Algebra
        else if line[0] == "add" {
            let resu = interpret(line[3].clone(),&mut var) + interpret(line[5].clone(),&mut var);
            var.insert(line[1][1..].to_string().clone(),resu);
        }
        else if line[0] == "sub" {
            let resu = interpret(line[3].clone(),&mut var) - interpret(line[5].clone(),&mut var);
            var.insert(line[1][1..].to_string().clone(),resu);
        }
        else if line[0] == "mul" {
            let resu = interpret(line[3].clone(),&mut var) * interpret(line[5].clone(),&mut var);
            var.insert(line[1][1..].to_string().clone(),resu);
        }
        else if line[0] == "div" {
            let resu = interpret(line[3].clone(),&mut var) / interpret(line[5].clone(),&mut var);
            var.insert(line[1][1..].to_string().clone(),resu);
        }
        else if line[0] == "mod" {
            let resu = interpret(line[3].clone(),&mut var) % interpret(line[5].clone(),&mut var);
            var.insert(line[1][1..].to_string().clone(),resu);
        }
        
        // Program flow control
        else if line[0] == "goto" {
            i = ((interpret(line[1].clone(),&mut var) as i64)- 2).try_into().unwrap();
        }
        else if line[0] == "skipif" {
            if cond(&line,&mut var) {
                let p : usize = ((interpret(line[4].clone(),&mut var) as i64)).try_into().unwrap();
                i += p
            }
        }
        else if line[0] == "doif" {
            if !cond(&line,&mut var) {
                let p : usize = ((interpret(line[4].clone(),&mut var) as i64)).try_into().unwrap();
                i += p
            }
        }

        // End program
        else if line[0] == "end" {
            break;
        }
        i += 1


    }
    println!("\n\nExecution complete!")
}
