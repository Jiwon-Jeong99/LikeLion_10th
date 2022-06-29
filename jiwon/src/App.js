import React from 'react'
// import Puang from "./puang"
import Box from "./Box"
import styled from "styled-components"
import "./App.css"

const StyledApp = styled.div
`
display:flex;
justify-content:center;
`
const StyledCard = styled.div
`
width:100vh;

`

const App = () => {
    return(
        <StyledApp>
            <StyledCard>
                <h3>인기중고</h3>
                <Box></Box>
                <Box></Box>
                <Box></Box>
            </StyledCard>
        </StyledApp>
    );
}

export default App