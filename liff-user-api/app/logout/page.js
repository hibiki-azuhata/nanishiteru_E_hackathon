"use client"
import { useEffect } from 'react'

const Logout = () => {
  useEffect(async () => {
    const liff = (await import('@line/liff')).default
    try {
      await liff.init({
        liffId: process.env.USER_LIFF_ID
      })
    } catch (error) {
      console.error('liff init error', error.message)
    }
    if (liff.isLoggedIn()) {
      liff.logout()
    }
  })
  return (
    <div>
        <h3>ログアウトに成功しました</h3>
        <h3>画面を閉じて下さい</h3>
    </div>
  )
}

export default Logout