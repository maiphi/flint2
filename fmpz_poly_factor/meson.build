
src_fmpz_poly_factor = ['CLD_mat.c', 'clear.c', 'concat.c', 'factor.c', 'factor_squarefree.c', 'factor_van_hoeij.c', 'factor_zassenhaus.c', 'factor_zassenhaus_recombination.c', 'fit_length.c', 'init.c', 'inlines.c', 'insert.c', 'print.c', 'realloc.c', 'set.c', 'van_hoeij_check_if_solved.c']

src_fmpz_poly_factor += generated_headers

headers_fmpz_poly_factor = files([])

headers += headers_fmpz_poly_factor

fmpz_poly_factor = static_library(
  'fmpz_poly_factor',
  src_fmpz_poly_factor,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
