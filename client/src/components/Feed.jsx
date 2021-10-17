import { useState } from "react";
import { Box, Grid } from "@mui/material";
import SideProfile from "./SideProfile";
import CreatePostModal from "./CreatePostModal";
import Post from "./Post";
import mockPosts from "../__mocks__/posts";
import CreateNewPostContainer from "./CreateNewPostContainer";

const Feed = (props) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [posts, setPosts] = useState([]);

  return (
    <Box display="flex" mx="20%" my="85px">
      <Grid container spacing={4} justifyContent="flex-start">
        <Grid item xs={8}>
          <CreateNewPostContainer setIsModalOpen={setIsModalOpen} />
          {mockPosts.map((post, idx) => (
            <Post
              key={idx}
              title={post.title}
              description={post.description}
              displayName={post.author.displayName}
              contentType={post.contentType}
              content={post.content}
              count={post.count}
              profileImage={post.author.profileImage}
              comments={post.comments}
            />
          ))}
        </Grid>
        <Grid
          display="flex"
          alignItems="flex-start"
          item
          xs={4}
          sx={{ marginTop: 1 }}
        >
          <SideProfile recentAuthors={props.recentAuthors} />
        </Grid>
      </Grid>
      <CreatePostModal
        isModalOpen={isModalOpen}
        setIsModalOpen={setIsModalOpen}
      ></CreatePostModal>
    </Box>
  );
};

export default Feed;
