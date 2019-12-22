//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    inputShowed: false,
    inputVal: "",
    background: [ ],
    indicatorDots: true,
    vertical: false,
    autoplay: false,
    interval: 2000,
    duration: 500,
    searchValue: ''
  },
  
  onShareAppMessage() {
    return {
      title: 'swiper',
      path: 'page/component/pages/swiper/swiper'
    }
  },
  onLoad: function (options) {
    if (options && options.searchValue) {
      this.setData({
        searchValue: "搜索：" + options.searchValue
      });
    }
  },
  wxSearchTab: function () {
    wx.redirectTo({
      url: '../search/search'
    })
  },
  showInput: function () {
    
  },
  hideInput: function () {
    
  },
  clearInput: function () {
   
  },
  inputTyping: function (e) {
   
  }
});
