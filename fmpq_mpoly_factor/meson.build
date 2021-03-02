
src_fmpq_mpoly_factor = files(['clear.c', 'expand.c', 'factor.c', 'factor_make_integral.c', 'factor_make_monic.c', 'factor_squarefree.c', 'fit_length.c', 'init.c', 'inlines.c', 'realloc.c', 'sort.c', 'swap_fmpz_mpoly_factor.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpq_mpoly_factor
else
  src_fmpq_mpoly_factor += generated_headers
  fmpq_mpoly_factor = static_library(
    'fmpq_mpoly_factor',
    src_fmpq_mpoly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpq_mpoly_factor
endif
