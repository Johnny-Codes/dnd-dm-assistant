import { useState } from "react";
import { useCreateNpcMutation } from "./npcApi";

const CreateNpcForm = () => {
  const [isCreating, setIsCreating] = useState(false);
  const [createNpc] = useCreateNpcMutation();

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsCreating(true);
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    console.log(data, typeof data);
    await createNpc(data);
    setIsCreating(false);
  };

  const spinnerStyle = {
    border: "4px solid rgba(0, 0, 0, 0.1)",
    borderLeftColor: "#000",
    borderRadius: "50%",
    width: "24px",
    height: "24px",
    animation: "spin 1s linear infinite",
  };

  const keyframesStyle = `
        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }
    `;

  return (
    <div>
      {isCreating ? (
        <div>
          <div style={spinnerStyle}></div>
          <p>Creating your character...</p>
          <style>{keyframesStyle}</style>
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <p>
          <label htmlFor="work">Work: </label>
          <input type="text" name="work" />
          </p>
          <p>
          <label htmlFor="additional_information">Additional Information: </label>
          <input type="text" name="additional_information" />
          </p>
          <p>
          <button type="submit">Submit</button>
          </p>
        </form>
      )}
    </div>
  );
};

export default CreateNpcForm;