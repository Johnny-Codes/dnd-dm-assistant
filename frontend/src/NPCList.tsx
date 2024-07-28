import { useState } from "react";
import { useGetNpcsQuery } from "./npcApi";
import CreateNpcForm from "./CreateNpcForm";

const NPCList = () => {
  const [visibleNpcIds, setVisibleNpcIds] = useState([]);

  const { data, error, isLoading } = useGetNpcsQuery();
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      {data?.map((npc) => (
        <div key={npc.id}>
          <div
            onClick={() => toggleVisibility(npc.id)}
            style={{ cursor: "pointer" }}
          >
            {visibleNpcIds.includes(npc.id) ? "▼" : "▶"} {npc.name}
          </div>
          {visibleNpcIds.includes(npc.id) && (
            <div>
              <p>
                <button>Edit</button> <button>Details</button>
              </p>
              <p>Race: {npc.race}</p>
              <p>Personality: {npc.personality}</p>
              <p>Physical Description: {npc.physical_description}</p>
              <div>
                Role Playing Tips:
                <ul>
                  {npc.role_playing_tips.map((tip) => (
                    <li key={tip.id}>{tip.tip}</li>
                  ))}
                </ul>
              </div>
            </div>
          )}
        </div>
      ))}

      <CreateNpcForm />
    </div>
  );
};

export default NPCList;
