
src_fq_templates = files(['div.c', 'is_invertible.c', 'is_invertible_f.c', 'is_square.c', 'multiplicative_order.c', 'sqrt.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_templates
else
  src_fq_templates += generated_headers
  fq_templates = static_library(
    'fq_templates',
    src_fq_templates,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_templates
endif
