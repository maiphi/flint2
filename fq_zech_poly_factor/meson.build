
src_fq_zech_poly_factor = ['clear.c', 'concat.c', 'factor.c', 'factor_berlekamp.c', 'factor_cantor_zassenhaus.c', 'factor_distinct_deg.c', 'factor_equal_deg.c', 'factor_equal_deg_prob.c', 'factor_kaltofen_shoup.c', 'factor_split_single.c', 'factor_squarefree.c', 'fit_length.c', 'init.c', 'inlines.c', 'insert.c', 'is_irreducible.c', 'is_irreducible_ben_or.c', 'is_irreducible_ddf.c', 'is_squarefree.c', 'iterated_frobenius_preinv.c', 'pow.c', 'print.c', 'print_pretty.c', 'realloc.c', 'set.c']

src_fq_zech_poly_factor += generated_headers

headers_fq_zech_poly_factor = files([])

headers += headers_fq_zech_poly_factor

fq_zech_poly_factor = static_library(
  'fq_zech_poly_factor',
  src_fq_zech_poly_factor,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
