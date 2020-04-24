
src_fmpz_poly_q = ['add.c', 'addmul.c', 'canonicalise.c', 'clear.c', 'derivative.c', 'div.c', 'evaluate.c', 'get_str.c', 'get_str_pretty.c', 'init.c', 'inlines.c', 'inv.c', 'is_canonical.c', 'mul.c', 'pow.c', 'print.c', 'print_pretty.c', 'randtest.c', 'scalar_div_mpq.c', 'scalar_div_mpz.c', 'scalar_div_si.c', 'scalar_mul_mpq.c', 'scalar_mul_mpz.c', 'scalar_mul_si.c', 'set.c', 'set_si.c', 'set_str.c', 'sub.c', 'submul.c', 'swap.c']

src_fmpz_poly_q += generated_headers

headers_fmpz_poly_q = files([])

headers += headers_fmpz_poly_q

fmpz_poly_q = static_library(
  'fmpz_poly_q',
  src_fmpz_poly_q,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
