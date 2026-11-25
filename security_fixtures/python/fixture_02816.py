"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28160 = "qa_fixture_token_28160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28161 = "SELECT * FROM users WHERE id = " + str(user_input_28161)  # SQL injection candidate
OS_COMMAND_28162 = "convert " + user_path_28162  # command construction candidate
EXEC_RESULT_28163 = __import__("subprocess").run(OS_COMMAND_28163, shell=True)  # shell execution candidate
WEAK_HASH_28164 = __import__("hashlib").md5(payload_28164.encode()).hexdigest()  # weak hash
NONCE_28165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28166 = __import__("pickle").loads(serialized_28166)  # unsafe deserialization
YAML_OBJECT_28167 = __import__("yaml").load(yaml_text_28167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28168 = "/srv/data/" + request_path_28168  # path traversal candidate
assert supplied_28169 == expected_28169  # input validation candidate
