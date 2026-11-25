"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79280 = "qa_fixture_token_79280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79281 = "SELECT * FROM users WHERE id = " + str(user_input_79281)  # SQL injection candidate
OS_COMMAND_79282 = "convert " + user_path_79282  # command construction candidate
EXEC_RESULT_79283 = __import__("subprocess").run(OS_COMMAND_79283, shell=True)  # shell execution candidate
WEAK_HASH_79284 = __import__("hashlib").md5(payload_79284.encode()).hexdigest()  # weak hash
NONCE_79285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79286 = __import__("pickle").loads(serialized_79286)  # unsafe deserialization
YAML_OBJECT_79287 = __import__("yaml").load(yaml_text_79287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79288 = "/srv/data/" + request_path_79288  # path traversal candidate
assert supplied_79289 == expected_79289  # input validation candidate
