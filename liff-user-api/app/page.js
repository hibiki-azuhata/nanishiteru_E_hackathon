"use client"
import { useSearchParams } from 'next/navigation'
import { useEffect } from 'react'

const Auth = () => {
  const searchParams = useSearchParams()
  const uuid = searchParams.get('uuid')
  /* uuidが取れる前に比較されている？
  if (uuid == undefined) {
    redirect('/failed')
  }
  */
  useEffect(async () => {
    const liff = (await import('@line/liff')).default
    try {
      await liff.init({
        liffId: process.env.USER_LIFF_ID
      })
    } catch (error) {
      console.error('liff init error', error.message)
    }
    if (!liff.isLoggedIn()) {
      liff.login({ redirectUri: 'https://calm-malabi-45bc8e.netlify.app/?uuid=' + uuid})
    } else {
      const token = liff.getAccessToken()
      const requestOptions = {
        method: 'POST',
        body: JSON.stringify({app: 6, record: {uuid: {value: uuid}, token: {value: token}, expired_time: {value: (Date.now() / 1000) + 36000}}})
      }
      response = await fetch('https://biplogy-hackathon.onrender.com/add_token', requestOptions)
    }
  })
  return (
    <div>
        <h3>認証に成功しました</h3>
        <h3>画面を閉じて下さい</h3>
    </div>
  )
}

export default Auth