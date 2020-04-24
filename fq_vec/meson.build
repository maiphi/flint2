
src_fq_vec = ['add.c', 'clear.c', 'dot.c', 'equal.c', 'fprint.c', 'init.c', 'inlines.c', 'is_zero.c', 'neg.c', 'randtest.c', 'scalar_addmul_fq.c', 'scalar_mul_fq.c', 'scalar_submul_fq.c', 'set.c', 'sub.c', 'swap.c', 'zero.c']

src_fq_vec += generated_headers

headers_fq_vec = files([])

headers += headers_fq_vec

fq_vec = static_library(
  'fq_vec',
  src_fq_vec,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
