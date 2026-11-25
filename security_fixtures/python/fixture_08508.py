"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85080 = "qa_fixture_token_85080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85081 = "SELECT * FROM users WHERE id = " + str(user_input_85081)  # SQL injection candidate
OS_COMMAND_85082 = "convert " + user_path_85082  # command construction candidate
EXEC_RESULT_85083 = __import__("subprocess").run(OS_COMMAND_85083, shell=True)  # shell execution candidate
WEAK_HASH_85084 = __import__("hashlib").md5(payload_85084.encode()).hexdigest()  # weak hash
NONCE_85085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85086 = __import__("pickle").loads(serialized_85086)  # unsafe deserialization
YAML_OBJECT_85087 = __import__("yaml").load(yaml_text_85087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85088 = "/srv/data/" + request_path_85088  # path traversal candidate
assert supplied_85089 == expected_85089  # input validation candidate
