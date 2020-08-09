
src_nmod_vec = files(['add.c', 'discrete_log_pohlig_hellman.c', 'dot.c', 'dot_bound_limbs.c', 'dot_ptr.c', 'inlines.c', 'max_bits.c', 'neg.c', 'randtest.c', 'reduce.c', 'scalar_addmul_nmod.c', 'scalar_mul_nmod.c', 'scalar_mul_nmod_shoup.c', 'sub.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_nmod_vec
else
  src_nmod_vec += generated_headers
  nmod_vec = static_library(
    'nmod_vec',
    src_nmod_vec,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += nmod_vec
endif
