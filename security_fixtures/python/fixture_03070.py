"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30700 = "qa_fixture_token_30700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30701 = "SELECT * FROM users WHERE id = " + str(user_input_30701)  # SQL injection candidate
OS_COMMAND_30702 = "convert " + user_path_30702  # command construction candidate
EXEC_RESULT_30703 = __import__("subprocess").run(OS_COMMAND_30703, shell=True)  # shell execution candidate
WEAK_HASH_30704 = __import__("hashlib").md5(payload_30704.encode()).hexdigest()  # weak hash
NONCE_30705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30706 = __import__("pickle").loads(serialized_30706)  # unsafe deserialization
YAML_OBJECT_30707 = __import__("yaml").load(yaml_text_30707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30708 = "/srv/data/" + request_path_30708  # path traversal candidate
assert supplied_30709 == expected_30709  # input validation candidate
