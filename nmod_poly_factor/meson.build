
src_nmod_poly_factor = files(['clear.c', 'concat.c', 'factor.c', 'factor_berlekamp.c', 'factor_cantor_zassenhaus.c', 'factor_distinct_deg.c', 'factor_distinct_deg_threaded.c', 'factor_equal_deg.c', 'factor_equal_deg_prob.c', 'factor_kaltofen_shoup.c', 'factor_squarefree.c', 'fit_length.c', 'init.c', 'inlines.c', 'insert.c', 'is_irreducible.c', 'is_irreducible_ddf.c', 'is_irreducible_rabin.c', 'is_squarefree.c', 'pow.c', 'print.c', 'realloc.c', 'set.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_nmod_poly_factor
else
  src_nmod_poly_factor += generated_headers
  nmod_poly_factor = static_library(
    'nmod_poly_factor',
    src_nmod_poly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += nmod_poly_factor
endif
