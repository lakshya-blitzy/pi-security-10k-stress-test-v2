"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50180 = "qa_fixture_token_50180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50181 = "SELECT * FROM users WHERE id = " + str(user_input_50181)  # SQL injection candidate
OS_COMMAND_50182 = "convert " + user_path_50182  # command construction candidate
EXEC_RESULT_50183 = __import__("subprocess").run(OS_COMMAND_50183, shell=True)  # shell execution candidate
WEAK_HASH_50184 = __import__("hashlib").md5(payload_50184.encode()).hexdigest()  # weak hash
NONCE_50185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50186 = __import__("pickle").loads(serialized_50186)  # unsafe deserialization
YAML_OBJECT_50187 = __import__("yaml").load(yaml_text_50187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50188 = "/srv/data/" + request_path_50188  # path traversal candidate
assert supplied_50189 == expected_50189  # input validation candidate
