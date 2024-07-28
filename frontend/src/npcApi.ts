import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const npcApi = createApi({
    baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api" }),
    reducerPath: "npcApi",
    tagTypes: ["npcs"],
    endpoints: (build) => ({
        getNpcs: build.query({
            query: () => "/npcs",
            providesTags: ["npcs"],
        }),
        createNpc: build.mutation({
            query: (npc) => ({
                url: "/npcs",
                method: "POST",
                body: npc,
            }),
            invalidatesTags: ["npcs"],
        }),
    }),
});

export const { useGetNpcsQuery, useCreateNpcMutation } = npcApi;