
src_fmpz_poly_q = files(['add.c', 'addmul.c', 'canonicalise.c', 'clear.c', 'derivative.c', 'div.c', 'evaluate.c', 'get_str.c', 'get_str_pretty.c', 'init.c', 'inlines.c', 'inv.c', 'is_canonical.c', 'mul.c', 'pow.c', 'print.c', 'print_pretty.c', 'randtest.c', 'scalar_div_mpq.c', 'scalar_div_mpz.c', 'scalar_div_si.c', 'scalar_mul_mpq.c', 'scalar_mul_mpz.c', 'scalar_mul_si.c', 'set.c', 'set_si.c', 'set_str.c', 'sub.c', 'submul.c', 'swap.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_poly_q
else
  src_fmpz_poly_q += generated_headers
  fmpz_poly_q = static_library(
    'fmpz_poly_q',
    src_fmpz_poly_q,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_poly_q
endif
