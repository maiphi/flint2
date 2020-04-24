
src_thread_pool = ['clear.c', 'get_size.c', 'give_back.c', 'init.c', 'request.c', 'restore_affinity.c', 'set_affinity.c', 'set_size.c', 'wait.c', 'wake.c']

src_thread_pool += generated_headers

headers_thread_pool = files([])

headers += headers_thread_pool

thread_pool = static_library(
  'thread_pool',
  src_thread_pool,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
