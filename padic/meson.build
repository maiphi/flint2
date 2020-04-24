
src_padic = ['add.c', 'clear.c', 'ctx_clear.c', 'ctx_init.c', 'div.c', 'exp.c', 'exp_balanced.c', 'exp_rectangular.c', 'fprint.c', 'get_fmpq.c', 'get_fmpz.c', 'get_mpq.c', 'get_mpz.c', 'get_str.c', 'init.c', 'inlines.c', 'inv.c', 'lifts.c', 'log.c', 'log_balanced.c', 'log_rectangular.c', 'log_satoh.c', 'mul.c', 'neg.c', 'pow_si.c', 'randtest.c', 'reduce.c', 'set.c', 'set_fmpq.c', 'set_fmpz.c', 'set_mpq.c', 'set_mpz.c', 'set_si.c', 'set_ui.c', 'shift.c', 'sqrt.c', 'sub.c', 'teichmuller.c', 'val_fac.c']

src_padic += generated_headers

headers_padic = files([])

headers += headers_padic

padic = static_library(
  'padic',
  src_padic,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
