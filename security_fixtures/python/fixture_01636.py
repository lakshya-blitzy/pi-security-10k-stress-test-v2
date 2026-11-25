"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16360 = "qa_fixture_token_16360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16361 = "SELECT * FROM users WHERE id = " + str(user_input_16361)  # SQL injection candidate
OS_COMMAND_16362 = "convert " + user_path_16362  # command construction candidate
EXEC_RESULT_16363 = __import__("subprocess").run(OS_COMMAND_16363, shell=True)  # shell execution candidate
WEAK_HASH_16364 = __import__("hashlib").md5(payload_16364.encode()).hexdigest()  # weak hash
NONCE_16365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16366 = __import__("pickle").loads(serialized_16366)  # unsafe deserialization
YAML_OBJECT_16367 = __import__("yaml").load(yaml_text_16367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16368 = "/srv/data/" + request_path_16368  # path traversal candidate
assert supplied_16369 == expected_16369  # input validation candidate
