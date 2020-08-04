
src_padic_mat = files(['add.c', 'canonicalise.c', 'clear.c', 'equal.c', 'fprint.c', 'fprint_pretty.c', 'get_entry_padic.c', 'get_fmpq_mat.c', 'init.c', 'inlines.c', 'is_zero.c', 'mul.c', 'neg.c', 'one.c', 'randtest.c', 'reduce.c', 'scalar_div_fmpz.c', 'scalar_mul_fmpz.c', 'scalar_mul_padic.c', 'set.c', 'set_entry_padic.c', 'set_fmpq_mat.c', 'sub.c', 'swap.c', 'transpose.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_padic_mat
else
  src_padic_mat += generated_headers
  padic_mat = static_library(
    'padic_mat',
    src_padic_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += padic_mat
endif
