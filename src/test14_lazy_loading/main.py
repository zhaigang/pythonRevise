from lazy_loading import LazyLoader

ll_obj = LazyLoader('plugs.show_graph', 'ShowGraph', {'image_path': '/tmp/images/test1.img'})
ll_obj.show()
ll_obj.update_iamge_path("/tmp/images/test2.img")
ll_obj.show()