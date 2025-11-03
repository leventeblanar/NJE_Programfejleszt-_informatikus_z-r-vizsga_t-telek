<h2>Binary as a term</h2>

I had some issues with remembering binary in every context as it is not that consistent everywhere, so I made a bit of a helper for it.

<h4>Binary as the numeral system</h4>
- binary (base-2): 0 and 1
- this is where bit/byte concepts come from
- Examples bitwise ops, masks, flags

<h4>Binary file (non-text)</h4>
- not human readable text, raw bytes (PNG, PDF, EXE, ELF, Mach-O)
- Implication: diff/merge is tricky, you need special tools (hexdump)

<h4>Executable "binary" (compiled program)</h4>
- a "binary" = a native executable or library (Windows: .exe/.dll, Linux: ELF, macOS: Mach-O)
- GO: AOT compliation to native machine code -> often a single (mostly statuc executable)
- C/C++/Rust: also produce native binaries
- Java/.NET: typically bytecode+ VM/JIT -> not "native" by default, but native builds exist

<h4>"Binary" package/wheel (Python ecodsystem)</h4>
- -binary/ [binary] means: prebuilt package including native code and dependencies (psycopg[binary])
- pros: fast install, no local compilation
- cons: bundled native libs -> updates/compat can be harder, for prod you often prefer a source build linked to system libs (psycopg[c])

<h4>Binary format / protocol</h4>
- binary protocol/serialization: byte-oriented, compact (e.g., Protobuf, Avro)
- Versus: text formats like JSON/YAML (more human friendly, larger/slower)

<h4>Binary logic /"two-ness"</h4>
- Binary value = two-valued (boolean: true/false)
- Binary opreator = rakes two operands (eg., a + b)
- Binary search/tree = "split in two / two children" - called binary due to the two-way structure, not because of 0/1
