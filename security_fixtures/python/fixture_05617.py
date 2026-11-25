"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56170 = "qa_fixture_token_56170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56171 = "SELECT * FROM users WHERE id = " + str(user_input_56171)  # SQL injection candidate
OS_COMMAND_56172 = "convert " + user_path_56172  # command construction candidate
EXEC_RESULT_56173 = __import__("subprocess").run(OS_COMMAND_56173, shell=True)  # shell execution candidate
WEAK_HASH_56174 = __import__("hashlib").md5(payload_56174.encode()).hexdigest()  # weak hash
NONCE_56175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56176 = __import__("pickle").loads(serialized_56176)  # unsafe deserialization
YAML_OBJECT_56177 = __import__("yaml").load(yaml_text_56177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56178 = "/srv/data/" + request_path_56178  # path traversal candidate
assert supplied_56179 == expected_56179  # input validation candidate
