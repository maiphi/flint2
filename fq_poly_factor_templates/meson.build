
src_fq_poly_factor_templates = files(['clear.c', 'concat.c', 'factor.c', 'factor_berlekamp.c', 'factor_cantor_zassenhaus.c', 'factor_distinct_deg.c', 'factor_equal_deg.c', 'factor_equal_deg_prob.c', 'factor_kaltofen_shoup.c', 'factor_split_single.c', 'factor_squarefree.c', 'fit_length.c', 'init.c', 'insert.c', 'is_irreducible.c', 'is_irreducible_ben_or.c', 'is_irreducible_ddf.c', 'is_squarefree.c', 'iterated_frobenius_preinv.c', 'pow.c', 'print.c', 'print_pretty.c', 'realloc.c', 'roots.c', 'set.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_poly_factor_templates
else
  src_fq_poly_factor_templates += generated_headers
  fq_poly_factor_templates = static_library(
    'fq_poly_factor_templates',
    src_fq_poly_factor_templates,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_poly_factor_templates
endif
