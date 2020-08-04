
src_fq_zech = files(['add.c', 'bit_pack.c', 'bit_unpack.c', 'clear.c', 'ctx_clear.c', 'ctx_randtest.c', 'ctx_randtest_reducible.c', 'div.c', 'frobenius.c', 'gcdinv.c', 'get_fq_nmod.c', 'get_set_fmpz_mod_mat.c', 'inlines.c', 'inv.c', 'is_invertible.c', 'is_invertible_f.c', 'mul.c', 'mul_fmpz.c', 'mul_si.c', 'mul_ui.c', 'multiplicative_order.c', 'neg.c', 'norm.c', 'pow.c', 'pth_root.c', 'randtest.c', 'set_fmpz.c', 'set_fq_nmod.c', 'sqr.c', 'sub.c', 'sub_one.c', 'trace.c', 'ctx_init.c', 'get_nmod_poly.c', 'get_str.c', 'get_str_pretty.c', 'is_square.c', 'rand.c', 'set_nmod_poly.c', 'sqrt.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_zech
else
  src_fq_zech += generated_headers
  fq_zech = static_library(
    'fq_zech',
    src_fq_zech,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_zech
endif
