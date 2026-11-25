"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50360 = "qa_fixture_token_50360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50361 = "SELECT * FROM users WHERE id = " + str(user_input_50361)  # SQL injection candidate
OS_COMMAND_50362 = "convert " + user_path_50362  # command construction candidate
EXEC_RESULT_50363 = __import__("subprocess").run(OS_COMMAND_50363, shell=True)  # shell execution candidate
WEAK_HASH_50364 = __import__("hashlib").md5(payload_50364.encode()).hexdigest()  # weak hash
NONCE_50365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50366 = __import__("pickle").loads(serialized_50366)  # unsafe deserialization
YAML_OBJECT_50367 = __import__("yaml").load(yaml_text_50367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50368 = "/srv/data/" + request_path_50368  # path traversal candidate
assert supplied_50369 == expected_50369  # input validation candidate
