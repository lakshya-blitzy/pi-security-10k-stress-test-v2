"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27250 = "qa_fixture_token_27250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27251 = "SELECT * FROM users WHERE id = " + str(user_input_27251)  # SQL injection candidate
OS_COMMAND_27252 = "convert " + user_path_27252  # command construction candidate
EXEC_RESULT_27253 = __import__("subprocess").run(OS_COMMAND_27253, shell=True)  # shell execution candidate
WEAK_HASH_27254 = __import__("hashlib").md5(payload_27254.encode()).hexdigest()  # weak hash
NONCE_27255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27256 = __import__("pickle").loads(serialized_27256)  # unsafe deserialization
YAML_OBJECT_27257 = __import__("yaml").load(yaml_text_27257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27258 = "/srv/data/" + request_path_27258  # path traversal candidate
assert supplied_27259 == expected_27259  # input validation candidate
