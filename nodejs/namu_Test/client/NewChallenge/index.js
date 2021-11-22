import React, { useState } from "react";
import styles from "./index.module.css";
import api from "../../apis/index.js";

export default function NewAlien(props) {
  // TODO: login 상태일 때만 접근할 수 있음
  // TODO: 챌린지에 접근 가능한 유저인지 확인해주어야 함
  const SELECT_DEFAULT = 0;
  const [challengeTitle, setChallengeTitle] = useState("");
  const [challengeDescription, setChallengeDescription] = useState("");
  const [challengeCapacity, setChallengeCapacity] = useState(SELECT_DEFAULT);
  const [challengeFrequency, setChallengeFrequency] = useState(SELECT_DEFAULT);
  const [challengeTag, setChallengeTag] = useState("");
  const [challengeMessage, setChallengeMessage] = useState(null);
  

  function handleChallengeTitle(e) {
    setChallengeTitle(e.target.value);
  }

  function handleChallengeDescription(e) {
    setChallengeDescription(e.target.value);
  }

  function handleChallengeCapacity(e) {
    setChallengeCapacity(e.target.value);
  }

  function handleChallengeFrequency(e) {
    setChallengeFrequency(e.target.value);
  }

  function handleChallengeTag(e) {
    setChallengeTag(e.target.value);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    // 입력하지 않은 것이 있는지 확인
    if (
      !validateChallenge(
        challengeTitle,
        challengeDescription,
        challengeCapacity,
        challengeFrequency
      )
    )
      return;
    
    setChallengeMessage(null);
    postChallenge();
  };

  function validateChallenge(
    challengeTitle,
    challengeDescription,
    challengeCapacity,
    challengeFrequency,
    challengeTag,
  ) {
    if (
      challengeTitle === "" ||
      challengeDescription === "" ||
      challengeCapacity === SELECT_DEFAULT ||
      challengeFrequency === SELECT_DEFAULT ||
      challengeTag === ""
    ) {
      setChallengeMessage("입력하지 않은 챌린지 정보가 있습니다.");
      return false;
    }

    setChallengeMessage(null);
    return true;
  }

  const postChallenge = async () => {
    let challengeData = {
      challenge_name: challengeTitle,
      challenge_content: challengeDescription,
      max_user: challengeCapacity,
      cnt_of_week: challengeFrequency,
      tag: challengeTag,
    };
    const res = await api.post("/challenge/create", challengeData);
    console.log("res", res);
    if (res.data.result === "success") {
      console.log("challengeData", challengeData);
      setChallengeTitle("");
      setChallengeDescription("");
      setChallengeCapacity(SELECT_DEFAULT);
      setChallengeFrequency(SELECT_DEFAULT);
      setChallengeTag("");
      alert("챌린지 생성에 성공하였습니다.");
      return;
    } else {
      console.log("challengeData", challengeData);
      setChallengeMessage("입력하지 않은 챌린지 정보가 있습니다.");
      return;
    }
  };

  return (
    <div class="flex justify-center items-center w-full bg-blue-400">
    <div class="w-1/2 bg-white rounded shadow-2xl p-8 m-4">
        <h1 class="block w-full text-center text-gray-800 text-2xl font-bold mb-6">Component Form</h1>
        <form action="/" method="post">
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="first_name">First Name</label>
                <input class="border py-2 px-3 text-grey-800" type="text" name="first_name" id="first_name" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="last_name">Last Name</label>
                <input class="border py-2 px-3 text-grey-800" type="text" name="last_name" id="last_name" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="email">Email</label>
                <input class="border py-2 px-3 text-grey-800" type="email" name="email" id="email" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="password">Password</label>
                <input class="border py-2 px-3 text-grey-800" type="password" name="password" id="password" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="Date">Date</label>
                <input class="border py-2 px-3 text-grey-800" type="date" name="date" id="date" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="File">File</label>
                <input class="border py-2 px-3 text-grey-800" type="file" name="file" id="file" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="color">Range</label>
                <input class="border py-2 text-grey-800" type="range" name="range" id="range" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="textarea">textarea</label>
                <textarea class="border py-2 px-3 text-grey-800" name="textarea" id="textarea"></textarea>
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="Select">Select</label>
                <select class="border py-2 px-3 text-grey-800">
                    <option>Surabaya</option>
                    <option>Jakarta</option>
                    <option>Bandung</option>
                    <option>Mojokerto</option>
                </select>
            </div>
            <button class="block bg-green-400 hover:bg-green-600 text-white uppercase text-lg mx-auto p-4 rounded" type="submit">Save</button>
        </form>
    </div>
</div>
  );
}
