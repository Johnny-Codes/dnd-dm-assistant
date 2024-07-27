import {configureStore} from '@reduxjs/toolkit'
import {npcApi} from './npcApi'

export const store = configureStore({
    reducer: {
        [npcApi.reducerPath]: npcApi.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(npcApi.middleware),
})

export type AppDispatch = typeof store.dispatch
export type RootState = ReturnType<typeof store.getState>