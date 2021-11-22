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
        <h1 class="block w-full text-center text-gray-800 text-2xl font-bold mb-6">새로운 챌린지 생성</h1>
        <form action="/" method="post">
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="first_name">First Name</label>
                <input class="border py-2 px-3 text-grey-800" type="text" name="first_name" id="first_name" />
            </div>
            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="textarea">textarea</label>
                <textarea class="border py-2 px-3 text-grey-800" name="textarea" id="textarea"></textarea>
            </div>

            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="color">Range</label>
                <input class="border py-2 text-grey-800" type="range" name="range" id="range" />
            </div>

            <div class="flex flex-col mb-4">
                <label class="mb-2 font-bold text-lg text-gray-900" for="Select">Select</label>
                <select class="border py-2 px-3 text-grey-800">
                <option value={SELECT_DEFAULT}>선택</option>
                <option value="7">매일 참여</option>
                <option value="6">주 6회 참여</option>
                <option value="5">주 5회 참여</option>
                <option value="4">주 4회 참여</option>
                <option value="3">주 3회 참여</option>
                <option value="2">주 2회 참여</option>
                <option value="1">주 1회 참여</option>
                </select>
            </div>

            <div class="main flex border rounded-full overflow-hidden m-4 select-none">
              <div class="title py-3 my-auto px-5 bg-blue-500 text-white text-sm font-semibold mr-3">Category</div>
              <label class="flex radio p-2 cursor-pointer">
                <input class="my-auto transform scale-125" type="radio" name="sfg" />
                <div class="title px-2">운동</div>
              </label>

              <label class="flex radio p-2 cursor-pointer">
                <input class="my-auto transform scale-125" type="radio" name="sfg" />
                <div class="title px-2">실생활</div>
              </label>

              <label class="flex radio p-2 cursor-pointer">
                <input class="my-auto transform scale-125" type="radio" name="sfg" />
                <div class="title px-2">공부</div>
              </label>

              <label class="flex radio p-2 cursor-pointer">
                <input class="my-auto transform scale-125" type="radio" name="sfg" />
                <div class="title px-2">독서</div>
              </label>

              <label class="flex radio p-2 cursor-pointer">
                <input class="my-auto transform scale-125" type="radio" name="sfg" />
                <div class="title px-2">기타</div>
              </label>
            </div>

            <button class="p-2 pl-5 pr-5 transition-colors duration-700 transform bg-indigo-500 hover:bg-blue-400 text-gray-100 text-lg rounded-lg focus:border-4 border-indigo-300" type="button" onClick={handleSubmit}>챌린지 생성</button>
        </form>
    </div>
</div>
  );
}
