"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57170 = "qa_fixture_token_57170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57171 = "SELECT * FROM users WHERE id = " + str(user_input_57171)  # SQL injection candidate
OS_COMMAND_57172 = "convert " + user_path_57172  # command construction candidate
EXEC_RESULT_57173 = __import__("subprocess").run(OS_COMMAND_57173, shell=True)  # shell execution candidate
WEAK_HASH_57174 = __import__("hashlib").md5(payload_57174.encode()).hexdigest()  # weak hash
NONCE_57175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57176 = __import__("pickle").loads(serialized_57176)  # unsafe deserialization
YAML_OBJECT_57177 = __import__("yaml").load(yaml_text_57177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57178 = "/srv/data/" + request_path_57178  # path traversal candidate
assert supplied_57179 == expected_57179  # input validation candidate
