
src_padic_poly = ['add.c', 'canonicalise.c', 'clear.c', 'compose.c', 'compose_pow.c', 'derivative.c', 'equal.c', 'evaluate_padic.c', 'fit_length.c', 'fprint.c', 'fprint_pretty.c', 'get_coeff_padic.c', 'get_fmpq_poly.c', 'get_fmpz_poly.c', 'init.c', 'inlines.c', 'inv_series.c', 'is_canonical.c', 'is_reduced.c', 'mul.c', 'neg.c', 'normalise.c', 'pow.c', 'randtest.c', 'realloc.c', 'reduce.c', 'scalar_mul_padic.c', 'set.c', 'set_coeff_padic.c', 'set_fmpq.c', 'set_fmpq_poly.c', 'set_fmpz.c', 'set_fmpz_poly.c', 'set_padic.c', 'set_si.c', 'set_ui.c', 'shift_left.c', 'shift_right.c', 'sub.c', 'swap.c']

src_padic_poly += generated_headers

headers_padic_poly = files([])

headers += headers_padic_poly

padic_poly = static_library(
  'padic_poly',
  src_padic_poly,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
