"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75190 = "qa_fixture_token_75190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75191 = "SELECT * FROM users WHERE id = " + str(user_input_75191)  # SQL injection candidate
OS_COMMAND_75192 = "convert " + user_path_75192  # command construction candidate
EXEC_RESULT_75193 = __import__("subprocess").run(OS_COMMAND_75193, shell=True)  # shell execution candidate
WEAK_HASH_75194 = __import__("hashlib").md5(payload_75194.encode()).hexdigest()  # weak hash
NONCE_75195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75196 = __import__("pickle").loads(serialized_75196)  # unsafe deserialization
YAML_OBJECT_75197 = __import__("yaml").load(yaml_text_75197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75198 = "/srv/data/" + request_path_75198  # path traversal candidate
assert supplied_75199 == expected_75199  # input validation candidate
