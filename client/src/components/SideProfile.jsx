import { useContext } from "react";
import { Box, Typography, Avatar, Stack, Link } from "@mui/material";
import AuthContext from "src/store/auth-context";
import { useNavigate } from "react-router-dom";

// Side profile displays the users avatar as well as display name.
// Underneath that, there is recently joined users that you can click on to go to their profile pages.
// This is rendered in the Feed.jsx file
const SideProfile = (props) => {
  const recentAuthors = props.recentAuthors;
  const authCtx = useContext(AuthContext);
  const navigate = useNavigate();
  return (
    <Box>
      <Stack direction="column" spacing={1}>
        <Stack alignItems="center" direction="row" spacing={2}>
          <Avatar
            alt="Avatar"
            src={authCtx.userdata.profileImage}
            sx={{ width: 56, height: 56 }}
            onClick={() => {
              const words = authCtx.userdata.id.split("/");
              const word = words[words.length - 1];
              navigate(`/app/author/${word}`, { state: authCtx.userdata });
            }}
            style={{ cursor: "pointer" }}
          />
          <Typography variant="h6">{authCtx.userdata.displayName}</Typography>
        </Stack>
        <Typography>Recently joined NewConnection:</Typography>
        {recentAuthors.map((author, idx) => (
          <Stack alignItems="center" direction="row" spacing={1} key={idx}>
            <Avatar
              alt="Avatar"
              src={author.profileImage}
              sx={{ width: 20, height: 20 }}
            />
            <Link
              component="button"
              variant="body2"
              underline="hover"
              onClick={() => {
                const words = author.id.split("/");
                const word = words[words.length - 1];
                navigate(`/app/author/${word}`, { state: author });
              }}
            >
              {author.displayName}
            </Link>
          </Stack>
        ))}
      </Stack>
    </Box>
  );
};

export default SideProfile;
