use std::env;
use std::fs;

fn make_folders_from_text_file(file_path: &str) {
    if let Ok(lines) = fs::read_to_string(file_path) {
        for line in lines.lines() {
            let folder_name = line.trim();
            if !fs::metadata(folder_name).is_ok() {
                fs::create_dir(folder_name).expect("Failed to create folder");
                println!("Created folder {}", folder_name);
            } else {
                println!("Folder {} already exists, skipping.", folder_name);
            }
        }
        println!("Complete");
    } else {
        println!("Failed to read file");
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        println!("Please specify a text file as a command line argument, e.g. 'text2folders filename.txt'");
        return;
    }
    let file_path = &args[1];
    make_folders_from_text_file(file_path);
}
