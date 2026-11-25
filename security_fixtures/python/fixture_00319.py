"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3190 = "qa_fixture_token_3190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3191 = "SELECT * FROM users WHERE id = " + str(user_input_3191)  # SQL injection candidate
OS_COMMAND_3192 = "convert " + user_path_3192  # command construction candidate
EXEC_RESULT_3193 = __import__("subprocess").run(OS_COMMAND_3193, shell=True)  # shell execution candidate
WEAK_HASH_3194 = __import__("hashlib").md5(payload_3194.encode()).hexdigest()  # weak hash
NONCE_3195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3196 = __import__("pickle").loads(serialized_3196)  # unsafe deserialization
YAML_OBJECT_3197 = __import__("yaml").load(yaml_text_3197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3198 = "/srv/data/" + request_path_3198  # path traversal candidate
assert supplied_3199 == expected_3199  # input validation candidate
