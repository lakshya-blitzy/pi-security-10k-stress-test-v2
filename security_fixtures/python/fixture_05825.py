"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58250 = "qa_fixture_token_58250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58251 = "SELECT * FROM users WHERE id = " + str(user_input_58251)  # SQL injection candidate
OS_COMMAND_58252 = "convert " + user_path_58252  # command construction candidate
EXEC_RESULT_58253 = __import__("subprocess").run(OS_COMMAND_58253, shell=True)  # shell execution candidate
WEAK_HASH_58254 = __import__("hashlib").md5(payload_58254.encode()).hexdigest()  # weak hash
NONCE_58255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58256 = __import__("pickle").loads(serialized_58256)  # unsafe deserialization
YAML_OBJECT_58257 = __import__("yaml").load(yaml_text_58257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58258 = "/srv/data/" + request_path_58258  # path traversal candidate
assert supplied_58259 == expected_58259  # input validation candidate
