## 실험목적

  곡 추천에 영향을 주는 요소에는 트랙의 재생시간(최신순), 트랙이 태그에 어울리는 정도(harmony), 태그자체의 인기도(score)가 있다.

 이 중 가장 큰 영향을 미치는 harmony와 score를 여러 방식으로 조정해보면서 추천 알고리즘에 적절하게 반영되는지 확인한다.

## 실험방법
  동일 디렉토리 안의 music/ 에서 서버를 작동한다
  
  이 music directory는 서비스되는 music 프로그램에서 실험에 불필요한 요소들을 배제하고 간략히 한 코드로 구성되어있다. 핵심 로직은 변하지 않았다.

  <code>python3 manage.py runserver 0.0.0.0:[portnum]

  다른 터미널을 열고

  <code>python3 test.py [experiment directory] [url]</code>

  * experiment1 : score는 같게, harmony를 다르게
 
  input.xlsz 참조

