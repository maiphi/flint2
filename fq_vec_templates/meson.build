
src_fq_vec_templates = ['add.c', 'clear.c', 'dot.c', 'equal.c', 'fprint.c', 'init.c', 'is_zero.c', 'neg.c', 'randtest.c', 'scalar_addmul_fq.c', 'scalar_mul_fq.c', 'scalar_submul_fq.c', 'set.c', 'sub.c', 'swap.c', 'zero.c']

src_fq_vec_templates += generated_headers

headers_fq_vec_templates = files([])

headers += headers_fq_vec_templates

fq_vec_templates = static_library(
  'fq_vec_templates',
  src_fq_vec_templates,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
