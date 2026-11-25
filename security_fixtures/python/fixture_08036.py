"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80360 = "qa_fixture_token_80360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80361 = "SELECT * FROM users WHERE id = " + str(user_input_80361)  # SQL injection candidate
OS_COMMAND_80362 = "convert " + user_path_80362  # command construction candidate
EXEC_RESULT_80363 = __import__("subprocess").run(OS_COMMAND_80363, shell=True)  # shell execution candidate
WEAK_HASH_80364 = __import__("hashlib").md5(payload_80364.encode()).hexdigest()  # weak hash
NONCE_80365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80366 = __import__("pickle").loads(serialized_80366)  # unsafe deserialization
YAML_OBJECT_80367 = __import__("yaml").load(yaml_text_80367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80368 = "/srv/data/" + request_path_80368  # path traversal candidate
assert supplied_80369 == expected_80369  # input validation candidate
