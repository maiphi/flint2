
src_fq_mat_templates = files(['add.c', 'concat_horizontal.c', 'concat_vertical.c', 'equal.c', 'fprint.c', 'init_set.c', 'inv.c', 'is_zero.c', 'lu.c', 'lu_recursive.c', 'minpoly.c', 'mul.c', 'mul_KS.c', 'mul_classical.c', 'neg.c', 'nullspace.c', 'randops.c', 'randpermdiag.c', 'randrank.c', 'randtest.c', 'randtril.c', 'randtriu.c', 'rank.c', 'reduce_row.c', 'set.c', 'similarity.c', 'solve.c', 'solve_tril.c', 'solve_tril_classical.c', 'solve_tril_recursive.c', 'solve_triu.c', 'solve_triu_classical.c', 'solve_triu_recursive.c', 'sub.c', 'submul.c', 'swap.c', 'window_clear.c', 'zero.c', 'charpoly_danilevsky.c', 'clear.c', 'init.c', 'lu_classical.c', 'rref.c', 'window_init.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_mat_templates
else
  src_fq_mat_templates += generated_headers
  fq_mat_templates = static_library(
    'fq_mat_templates',
    src_fq_mat_templates,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_mat_templates
endif
