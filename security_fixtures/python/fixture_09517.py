"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95170 = "qa_fixture_token_95170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95171 = "SELECT * FROM users WHERE id = " + str(user_input_95171)  # SQL injection candidate
OS_COMMAND_95172 = "convert " + user_path_95172  # command construction candidate
EXEC_RESULT_95173 = __import__("subprocess").run(OS_COMMAND_95173, shell=True)  # shell execution candidate
WEAK_HASH_95174 = __import__("hashlib").md5(payload_95174.encode()).hexdigest()  # weak hash
NONCE_95175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95176 = __import__("pickle").loads(serialized_95176)  # unsafe deserialization
YAML_OBJECT_95177 = __import__("yaml").load(yaml_text_95177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95178 = "/srv/data/" + request_path_95178  # path traversal candidate
assert supplied_95179 == expected_95179  # input validation candidate
