
src_qadic = ['ctx_clear.c', 'ctx_init.c', 'ctx_init_conway.c', 'exp.c', 'exp_balanced.c', 'exp_rectangular.c', 'fprint_pretty.c', 'frobenius.c', 'inlines.c', 'inv.c', 'log.c', 'log_balanced.c', 'log_rectangular.c', 'mul.c', 'norm.c', 'norm_analytic.c', 'norm_resultant.c', 'pow.c', 'set_fmpz_poly.c', 'sqrt.c', 'teichmuller.c', 'trace.c']

src_qadic += generated_headers

headers_qadic = files([])

headers += headers_qadic

qadic = static_library(
  'qadic',
  src_qadic,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
