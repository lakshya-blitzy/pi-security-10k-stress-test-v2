"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6170 = "qa_fixture_token_6170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6171 = "SELECT * FROM users WHERE id = " + str(user_input_6171)  # SQL injection candidate
OS_COMMAND_6172 = "convert " + user_path_6172  # command construction candidate
EXEC_RESULT_6173 = __import__("subprocess").run(OS_COMMAND_6173, shell=True)  # shell execution candidate
WEAK_HASH_6174 = __import__("hashlib").md5(payload_6174.encode()).hexdigest()  # weak hash
NONCE_6175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6176 = __import__("pickle").loads(serialized_6176)  # unsafe deserialization
YAML_OBJECT_6177 = __import__("yaml").load(yaml_text_6177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6178 = "/srv/data/" + request_path_6178  # path traversal candidate
assert supplied_6179 == expected_6179  # input validation candidate
