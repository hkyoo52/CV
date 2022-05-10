* mmseg github에 checkpoint는 모델 전체 구조가 잇는데 코드는 backbone만 불러오게 되어있음
    * key 앞에 backbone 전부 붙여서 로드했는데 size 문제 생김

* Size 문제 해결
    * single_gpu_test() 안에 들어가서 result = model(return_loss=False, **data) -> result = model(return_loss=False, rescale=False, **data)
    * https://github.com/open-mmlab/mmsegmentation/issues/1530#issuecomment-1115898338


* 근데 config를 수정해서 num_head를 바꾸는 방법 존재!!!

* num_classes=11일때 reduce_label_zero=True, num_classes=10 으로 학습해야 함 (11중 1개는 배경이니깐)
