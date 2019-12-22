//index.js
Page({
  data: {
    searchValue: ''
  },
  bindTap1: function (e) {
    wx.switchTab({
      url: '../index/index',
    })
  },
  // 搜索页面跳回
  onLoad: function (options) {
    if (options && options.searchValue) {
      this.setData({
        searchValue: "搜索：" + options.searchValue
      });
    }
  },

  // 搜索入口  
  wxSearchTab: function () {
    wx.redirectTo({
      url: '../search/search'
    })
  }
})
