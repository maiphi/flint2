
src_fmpz_poly_factor = files(['CLD_mat.c', 'clear.c', 'concat.c', 'factor_squarefree.c', 'factor_van_hoeij.c', 'fit_length.c', 'init.c', 'inlines.c', 'insert.c', 'print.c', 'realloc.c', 'set.c', 'van_hoeij_check_if_solved.c', 'factor.c', 'factor_quadratic.c', 'factor_zassenhaus.c', 'factor_zassenhaus_recombination.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_poly_factor
else
  src_fmpz_poly_factor += generated_headers
  fmpz_poly_factor = static_library(
    'fmpz_poly_factor',
    src_fmpz_poly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_poly_factor
endif
