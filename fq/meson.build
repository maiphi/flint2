
src_fq = files(['add.c', 'bit_pack.c', 'bit_unpack.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_conway.c', 'ctx_init_modulus.c', 'ctx_randtest.c', 'ctx_randtest_reducible.c', 'div.c', 'frobenius.c', 'gcdinv.c', 'get_set_fmpz_mod_mat.c', 'get_str.c', 'get_str_pretty.c', 'inlines.c', 'inv.c', 'is_invertible.c', 'is_invertible_f.c', 'mul.c', 'mul_fmpz.c', 'mul_si.c', 'mul_ui.c', 'multiplicative_order.c', 'neg.c', 'norm.c', 'pow.c', 'pow_ui.c', 'pth_root.c', 'randtest.c', 'sqr.c', 'sub.c', 'sub_one.c', 'trace.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq
else
  src_fq += generated_headers
  fq = static_library(
    'fq',
    src_fq,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq
endif
