import Header from "src/components/header/Header";
import { useParams, useLocation, Navigate } from "react-router-dom";
import Banner from "src/components/profile/Banner";
import ProfileFeed from "src/components/profile/ProfileFeed";
import { useState, useContext, useEffect } from "react";
import AuthContext from "src/store/auth-context";
import { Container } from "@mui/material";
import { authCredentials } from "src/utils/utils";

const Profile = () => {
  let { authorID } = useParams();
  const { state } = useLocation();
  const authCtx = useContext(AuthContext);
  const [following, setFollowing] = useState(false);
  const [isUser, setIsUser] = useState(false);

  // Checks if the id from the url matches the logged in user id
  // if it doesnt, we need to check if the logged in user is following the user id from the URL
  useEffect(() => {
    const fetchFollower = async () => {
      try {
        const words = authCtx.userdata.id.split("/");
        const authctxid = words[words.length - 1];
        let credentials = authCredentials(state.host);
        const response = await fetch(`${state.id}/followers/${authctxid}/`, {
          headers: {
            Authorization: `Basic ` + btoa(credentials),
          },
        });
        if (response.ok) {
          const data = await response.json();
          setFollowing(data === "true" ? true : false);
        }
      } catch (error) {
        setFollowing(false);
      }
    };
    if (state.id === authCtx.userdata.id) {
      setIsUser(true);
    } else {
      fetchFollower();
    }
  }, [state.id, state.host, authCtx.userdata.id]);

  return (
    <>
      <Header />
      {state ? (
        <Container maxWidth="sm" sx={{ px: 0 }}>
          <Banner
            authorID={authorID}
            author={state}
            isUser={isUser}
            following={following}
            setFollowing={setFollowing}
          />
          <ProfileFeed authorID={authorID} author={state} />
        </Container>
      ) : (
        <Navigate to="/404" replace={true} />
      )}
    </>
  );
};

export default Profile;
