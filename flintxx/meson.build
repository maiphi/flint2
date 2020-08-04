
src_flintxx = files(['dummy.c'])

headers += files(['default_rules.h', 'evaluation_tools.h', 'expression.h', 'expression_traits.h', 'flint_classes.h', 'flint_exception.h', 'forwarding.h', 'frandxx.h', 'ltuple.h', 'matrix.h', 'mp.h', 'rules.h', 'stdmath.h', 'traits.h', 'traits_fwd.h', 'tuple.h', 'vector.h'])

if meson.version().version_compare('>=0.55.0')
  src += src_flintxx
else
  src_flintxx += generated_headers
  flintxx = static_library(
    'flintxx',
    src_flintxx,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += flintxx
endif
