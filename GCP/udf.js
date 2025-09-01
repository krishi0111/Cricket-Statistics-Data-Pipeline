function transform(line) {
    if (!line) return null; // handle empty or undefined lines
    
    var values = line.split(',');
    
    if (values.length < 3) {
        console.error("Invalid CSV line:", line);
        return null;
    }

    var obj = {
        rank: values[0].trim(),
        name: values[1].trim(),
        country: values[2].trim()
    };

    return JSON.stringify(obj);
}
