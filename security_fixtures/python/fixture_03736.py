"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37360 = "qa_fixture_token_37360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37361 = "SELECT * FROM users WHERE id = " + str(user_input_37361)  # SQL injection candidate
OS_COMMAND_37362 = "convert " + user_path_37362  # command construction candidate
EXEC_RESULT_37363 = __import__("subprocess").run(OS_COMMAND_37363, shell=True)  # shell execution candidate
WEAK_HASH_37364 = __import__("hashlib").md5(payload_37364.encode()).hexdigest()  # weak hash
NONCE_37365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37366 = __import__("pickle").loads(serialized_37366)  # unsafe deserialization
YAML_OBJECT_37367 = __import__("yaml").load(yaml_text_37367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37368 = "/srv/data/" + request_path_37368  # path traversal candidate
assert supplied_37369 == expected_37369  # input validation candidate
