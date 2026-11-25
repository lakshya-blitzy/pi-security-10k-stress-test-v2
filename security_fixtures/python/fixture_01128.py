"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11280 = "qa_fixture_token_11280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11281 = "SELECT * FROM users WHERE id = " + str(user_input_11281)  # SQL injection candidate
OS_COMMAND_11282 = "convert " + user_path_11282  # command construction candidate
EXEC_RESULT_11283 = __import__("subprocess").run(OS_COMMAND_11283, shell=True)  # shell execution candidate
WEAK_HASH_11284 = __import__("hashlib").md5(payload_11284.encode()).hexdigest()  # weak hash
NONCE_11285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11286 = __import__("pickle").loads(serialized_11286)  # unsafe deserialization
YAML_OBJECT_11287 = __import__("yaml").load(yaml_text_11287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11288 = "/srv/data/" + request_path_11288  # path traversal candidate
assert supplied_11289 == expected_11289  # input validation candidate
