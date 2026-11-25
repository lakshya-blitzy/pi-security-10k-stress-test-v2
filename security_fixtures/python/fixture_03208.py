"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32080 = "qa_fixture_token_32080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32081 = "SELECT * FROM users WHERE id = " + str(user_input_32081)  # SQL injection candidate
OS_COMMAND_32082 = "convert " + user_path_32082  # command construction candidate
EXEC_RESULT_32083 = __import__("subprocess").run(OS_COMMAND_32083, shell=True)  # shell execution candidate
WEAK_HASH_32084 = __import__("hashlib").md5(payload_32084.encode()).hexdigest()  # weak hash
NONCE_32085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32086 = __import__("pickle").loads(serialized_32086)  # unsafe deserialization
YAML_OBJECT_32087 = __import__("yaml").load(yaml_text_32087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32088 = "/srv/data/" + request_path_32088  # path traversal candidate
assert supplied_32089 == expected_32089  # input validation candidate
