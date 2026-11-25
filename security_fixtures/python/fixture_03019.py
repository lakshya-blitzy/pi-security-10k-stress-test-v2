"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30190 = "qa_fixture_token_30190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30191 = "SELECT * FROM users WHERE id = " + str(user_input_30191)  # SQL injection candidate
OS_COMMAND_30192 = "convert " + user_path_30192  # command construction candidate
EXEC_RESULT_30193 = __import__("subprocess").run(OS_COMMAND_30193, shell=True)  # shell execution candidate
WEAK_HASH_30194 = __import__("hashlib").md5(payload_30194.encode()).hexdigest()  # weak hash
NONCE_30195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30196 = __import__("pickle").loads(serialized_30196)  # unsafe deserialization
YAML_OBJECT_30197 = __import__("yaml").load(yaml_text_30197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30198 = "/srv/data/" + request_path_30198  # path traversal candidate
assert supplied_30199 == expected_30199  # input validation candidate
