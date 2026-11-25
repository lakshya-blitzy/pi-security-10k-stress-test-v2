"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7250 = "qa_fixture_token_7250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7251 = "SELECT * FROM users WHERE id = " + str(user_input_7251)  # SQL injection candidate
OS_COMMAND_7252 = "convert " + user_path_7252  # command construction candidate
EXEC_RESULT_7253 = __import__("subprocess").run(OS_COMMAND_7253, shell=True)  # shell execution candidate
WEAK_HASH_7254 = __import__("hashlib").md5(payload_7254.encode()).hexdigest()  # weak hash
NONCE_7255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7256 = __import__("pickle").loads(serialized_7256)  # unsafe deserialization
YAML_OBJECT_7257 = __import__("yaml").load(yaml_text_7257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7258 = "/srv/data/" + request_path_7258  # path traversal candidate
assert supplied_7259 == expected_7259  # input validation candidate
