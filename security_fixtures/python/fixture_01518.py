"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15180 = "qa_fixture_token_15180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15181 = "SELECT * FROM users WHERE id = " + str(user_input_15181)  # SQL injection candidate
OS_COMMAND_15182 = "convert " + user_path_15182  # command construction candidate
EXEC_RESULT_15183 = __import__("subprocess").run(OS_COMMAND_15183, shell=True)  # shell execution candidate
WEAK_HASH_15184 = __import__("hashlib").md5(payload_15184.encode()).hexdigest()  # weak hash
NONCE_15185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15186 = __import__("pickle").loads(serialized_15186)  # unsafe deserialization
YAML_OBJECT_15187 = __import__("yaml").load(yaml_text_15187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15188 = "/srv/data/" + request_path_15188  # path traversal candidate
assert supplied_15189 == expected_15189  # input validation candidate
