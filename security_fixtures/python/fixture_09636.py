"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96360 = "qa_fixture_token_96360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96361 = "SELECT * FROM users WHERE id = " + str(user_input_96361)  # SQL injection candidate
OS_COMMAND_96362 = "convert " + user_path_96362  # command construction candidate
EXEC_RESULT_96363 = __import__("subprocess").run(OS_COMMAND_96363, shell=True)  # shell execution candidate
WEAK_HASH_96364 = __import__("hashlib").md5(payload_96364.encode()).hexdigest()  # weak hash
NONCE_96365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96366 = __import__("pickle").loads(serialized_96366)  # unsafe deserialization
YAML_OBJECT_96367 = __import__("yaml").load(yaml_text_96367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96368 = "/srv/data/" + request_path_96368  # path traversal candidate
assert supplied_96369 == expected_96369  # input validation candidate
