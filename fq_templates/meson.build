
src_fq_templates = ['div.c', 'is_invertible.c', 'is_invertible_f.c', 'multiplicative_order.c']

src_fq_templates += generated_headers

headers_fq_templates = files([])

headers += headers_fq_templates

fq_templates = static_library(
  'fq_templates',
  src_fq_templates,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
