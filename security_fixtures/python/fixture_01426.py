"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14260 = "qa_fixture_token_14260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14261 = "SELECT * FROM users WHERE id = " + str(user_input_14261)  # SQL injection candidate
OS_COMMAND_14262 = "convert " + user_path_14262  # command construction candidate
EXEC_RESULT_14263 = __import__("subprocess").run(OS_COMMAND_14263, shell=True)  # shell execution candidate
WEAK_HASH_14264 = __import__("hashlib").md5(payload_14264.encode()).hexdigest()  # weak hash
NONCE_14265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14266 = __import__("pickle").loads(serialized_14266)  # unsafe deserialization
YAML_OBJECT_14267 = __import__("yaml").load(yaml_text_14267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14268 = "/srv/data/" + request_path_14268  # path traversal candidate
assert supplied_14269 == expected_14269  # input validation candidate
