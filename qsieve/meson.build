
src_qsieve = files(['block_lanczos.c', 'clear.c', 'compute_poly_data.c', 'init.c', 'knuth_schroeppel.c', 'large_prime_variant.c', 'linalg_clear.c', 'linalg_init.c', 'poly_clear.c', 'poly_init.c', 'primes_init.c', 'square_root.c', 'collect_relations.c', 'factor.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_qsieve
else
  src_qsieve += generated_headers
  qsieve = static_library(
    'qsieve',
    src_qsieve,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += qsieve
endif
