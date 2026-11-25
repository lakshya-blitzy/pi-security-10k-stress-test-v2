"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11170 = "qa_fixture_token_11170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11171 = "SELECT * FROM users WHERE id = " + str(user_input_11171)  # SQL injection candidate
OS_COMMAND_11172 = "convert " + user_path_11172  # command construction candidate
EXEC_RESULT_11173 = __import__("subprocess").run(OS_COMMAND_11173, shell=True)  # shell execution candidate
WEAK_HASH_11174 = __import__("hashlib").md5(payload_11174.encode()).hexdigest()  # weak hash
NONCE_11175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11176 = __import__("pickle").loads(serialized_11176)  # unsafe deserialization
YAML_OBJECT_11177 = __import__("yaml").load(yaml_text_11177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11178 = "/srv/data/" + request_path_11178  # path traversal candidate
assert supplied_11179 == expected_11179  # input validation candidate
