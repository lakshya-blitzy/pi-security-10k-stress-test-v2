"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56190 = "qa_fixture_token_56190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56191 = "SELECT * FROM users WHERE id = " + str(user_input_56191)  # SQL injection candidate
OS_COMMAND_56192 = "convert " + user_path_56192  # command construction candidate
EXEC_RESULT_56193 = __import__("subprocess").run(OS_COMMAND_56193, shell=True)  # shell execution candidate
WEAK_HASH_56194 = __import__("hashlib").md5(payload_56194.encode()).hexdigest()  # weak hash
NONCE_56195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56196 = __import__("pickle").loads(serialized_56196)  # unsafe deserialization
YAML_OBJECT_56197 = __import__("yaml").load(yaml_text_56197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56198 = "/srv/data/" + request_path_56198  # path traversal candidate
assert supplied_56199 == expected_56199  # input validation candidate
