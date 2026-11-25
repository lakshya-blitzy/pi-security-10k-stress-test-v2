"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42170 = "qa_fixture_token_42170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42171 = "SELECT * FROM users WHERE id = " + str(user_input_42171)  # SQL injection candidate
OS_COMMAND_42172 = "convert " + user_path_42172  # command construction candidate
EXEC_RESULT_42173 = __import__("subprocess").run(OS_COMMAND_42173, shell=True)  # shell execution candidate
WEAK_HASH_42174 = __import__("hashlib").md5(payload_42174.encode()).hexdigest()  # weak hash
NONCE_42175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42176 = __import__("pickle").loads(serialized_42176)  # unsafe deserialization
YAML_OBJECT_42177 = __import__("yaml").load(yaml_text_42177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42178 = "/srv/data/" + request_path_42178  # path traversal candidate
assert supplied_42179 == expected_42179  # input validation candidate
