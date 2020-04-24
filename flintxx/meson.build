
src_flintxx = ['dummy.c']

src_flintxx += generated_headers

headers_flintxx = files(['default_rules.h', 'evaluation_tools.h', 'expression.h', 'expression_traits.h', 'flint_classes.h', 'flint_exception.h', 'forwarding.h', 'frandxx.h', 'ltuple.h', 'matrix.h', 'mp.h', 'rules.h', 'stdmath.h', 'traits.h', 'traits_fwd.h', 'tuple.h', 'vector.h'])

headers += headers_flintxx

flintxx = static_library(
  'flintxx',
  src_flintxx,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
