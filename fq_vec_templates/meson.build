
src_fq_vec_templates = files(['add.c', 'clear.c', 'dot.c', 'equal.c', 'fprint.c', 'init.c', 'is_zero.c', 'neg.c', 'randtest.c', 'scalar_addmul_fq.c', 'scalar_mul_fq.c', 'scalar_submul_fq.c', 'set.c', 'sub.c', 'swap.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_vec_templates
else
  src_fq_vec_templates += generated_headers
  fq_vec_templates = static_library(
    'fq_vec_templates',
    src_fq_vec_templates,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_vec_templates
endif
