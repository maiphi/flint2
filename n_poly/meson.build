
src_n_poly = files(['n_bpoly.c', 'n_bpoly_mod.c', 'n_bpoly_mod_gcd.c', 'n_bpoly_stack.c', 'n_fq.c', 'n_fq_bpoly.c', 'n_fq_bpoly_gcd.c', 'n_fq_bpoly_taylor_shift.c', 'n_fq_poly.c', 'n_fq_poly_add.c', 'n_fq_poly_add_si.c', 'n_fq_poly_divrem.c', 'n_fq_poly_gcd.c', 'n_fq_poly_inv_series.c', 'n_fq_poly_mul.c', 'n_fq_poly_mullow.c', 'n_fq_poly_mulmod.c', 'n_fq_poly_neg.c', 'n_fq_poly_pow.c', 'n_fq_poly_rem.c', 'n_fq_poly_sub.c', 'n_fq_poly_xgcd.c', 'n_fq_polyun.c', 'n_fq_pow_cache.c', 'n_poly.c', 'n_poly_mod.c', 'n_poly_stack.c', 'n_polyu.c', 'n_polyu1n_gcd.c', 'n_polyun.c', 'n_polyun_stack.c', 'n_tpoly.c', 'nmod_n_fq_interp.c', 'nmod_pow_cache.c', 'rbtree.c', 'zippel_helpers.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_n_poly
else
  src_n_poly += generated_headers
  n_poly = static_library(
    'n_poly',
    src_n_poly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += n_poly
endif
