// Decompress an Oodle Kraken DCX (DCX\0 ... KRAK) file: krak <in.dcx> <out>
// Optional: krak <in> <out> <data offset> <uncompressed size> for raw streams.
use std::io::Cursor;
fn main() {
    let a: Vec<String> = std::env::args().collect();
    if a.len() < 3 {
        eprintln!("usage: krak <in.dcx> <out> [offset size]");
        std::process::exit(2);
    }
    let data = std::fs::read(&a[1]).unwrap();
    let (off, len) = if a.len() >= 5 {
        (a[3].parse().unwrap(), a[4].parse().unwrap())
    } else {
        assert!(&data[..4] == b"DCX\0", "not a DCX file");
        let len = u32::from_be_bytes(data[0x1C..0x20].try_into().unwrap()) as usize;
        let dca = data.windows(4).position(|w| w == b"DCA\0").expect("no DCA block");
        (dca + 8, len)
    };
    let mut out = vec![0u8; len];
    let mut ex = oozextract::Extractor::new();
    let mut cur = Cursor::new(&data[off..]);
    let n = ex.read(&mut cur, &mut out).unwrap();
    std::fs::write(&a[2], &out[..n]).unwrap();
    println!("{} bytes", n);
}
