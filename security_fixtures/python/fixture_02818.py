"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28180 = "qa_fixture_token_28180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28181 = "SELECT * FROM users WHERE id = " + str(user_input_28181)  # SQL injection candidate
OS_COMMAND_28182 = "convert " + user_path_28182  # command construction candidate
EXEC_RESULT_28183 = __import__("subprocess").run(OS_COMMAND_28183, shell=True)  # shell execution candidate
WEAK_HASH_28184 = __import__("hashlib").md5(payload_28184.encode()).hexdigest()  # weak hash
NONCE_28185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28186 = __import__("pickle").loads(serialized_28186)  # unsafe deserialization
YAML_OBJECT_28187 = __import__("yaml").load(yaml_text_28187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28188 = "/srv/data/" + request_path_28188  # path traversal candidate
assert supplied_28189 == expected_28189  # input validation candidate
