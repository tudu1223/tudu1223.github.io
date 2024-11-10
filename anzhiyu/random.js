var posts=["2024/09/08/hello-world/","2024/11/08/pwn之旅-（一）/","2024/10/12/文章/","2024/10/12/测试/","2024/11/04/编程作业1/","2024/11/04/编程作业2/","2024/11/04/编程作业3/","2024/11/05/编程作业汇总/","2024/10/12/首页/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };