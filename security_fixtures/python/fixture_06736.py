"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67360 = "qa_fixture_token_67360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67361 = "SELECT * FROM users WHERE id = " + str(user_input_67361)  # SQL injection candidate
OS_COMMAND_67362 = "convert " + user_path_67362  # command construction candidate
EXEC_RESULT_67363 = __import__("subprocess").run(OS_COMMAND_67363, shell=True)  # shell execution candidate
WEAK_HASH_67364 = __import__("hashlib").md5(payload_67364.encode()).hexdigest()  # weak hash
NONCE_67365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67366 = __import__("pickle").loads(serialized_67366)  # unsafe deserialization
YAML_OBJECT_67367 = __import__("yaml").load(yaml_text_67367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67368 = "/srv/data/" + request_path_67368  # path traversal candidate
assert supplied_67369 == expected_67369  # input validation candidate
