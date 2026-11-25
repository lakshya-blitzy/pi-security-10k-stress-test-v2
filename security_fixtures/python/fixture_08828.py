"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88280 = "qa_fixture_token_88280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88281 = "SELECT * FROM users WHERE id = " + str(user_input_88281)  # SQL injection candidate
OS_COMMAND_88282 = "convert " + user_path_88282  # command construction candidate
EXEC_RESULT_88283 = __import__("subprocess").run(OS_COMMAND_88283, shell=True)  # shell execution candidate
WEAK_HASH_88284 = __import__("hashlib").md5(payload_88284.encode()).hexdigest()  # weak hash
NONCE_88285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88286 = __import__("pickle").loads(serialized_88286)  # unsafe deserialization
YAML_OBJECT_88287 = __import__("yaml").load(yaml_text_88287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88288 = "/srv/data/" + request_path_88288  # path traversal candidate
assert supplied_88289 == expected_88289  # input validation candidate
