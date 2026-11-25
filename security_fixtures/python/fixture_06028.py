"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60280 = "qa_fixture_token_60280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60281 = "SELECT * FROM users WHERE id = " + str(user_input_60281)  # SQL injection candidate
OS_COMMAND_60282 = "convert " + user_path_60282  # command construction candidate
EXEC_RESULT_60283 = __import__("subprocess").run(OS_COMMAND_60283, shell=True)  # shell execution candidate
WEAK_HASH_60284 = __import__("hashlib").md5(payload_60284.encode()).hexdigest()  # weak hash
NONCE_60285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60286 = __import__("pickle").loads(serialized_60286)  # unsafe deserialization
YAML_OBJECT_60287 = __import__("yaml").load(yaml_text_60287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60288 = "/srv/data/" + request_path_60288  # path traversal candidate
assert supplied_60289 == expected_60289  # input validation candidate
