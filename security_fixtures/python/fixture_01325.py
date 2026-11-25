"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13250 = "qa_fixture_token_13250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13251 = "SELECT * FROM users WHERE id = " + str(user_input_13251)  # SQL injection candidate
OS_COMMAND_13252 = "convert " + user_path_13252  # command construction candidate
EXEC_RESULT_13253 = __import__("subprocess").run(OS_COMMAND_13253, shell=True)  # shell execution candidate
WEAK_HASH_13254 = __import__("hashlib").md5(payload_13254.encode()).hexdigest()  # weak hash
NONCE_13255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13256 = __import__("pickle").loads(serialized_13256)  # unsafe deserialization
YAML_OBJECT_13257 = __import__("yaml").load(yaml_text_13257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13258 = "/srv/data/" + request_path_13258  # path traversal candidate
assert supplied_13259 == expected_13259  # input validation candidate
