"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11450 = "qa_fixture_token_11450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11451 = "SELECT * FROM users WHERE id = " + str(user_input_11451)  # SQL injection candidate
OS_COMMAND_11452 = "convert " + user_path_11452  # command construction candidate
EXEC_RESULT_11453 = __import__("subprocess").run(OS_COMMAND_11453, shell=True)  # shell execution candidate
WEAK_HASH_11454 = __import__("hashlib").md5(payload_11454.encode()).hexdigest()  # weak hash
NONCE_11455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11456 = __import__("pickle").loads(serialized_11456)  # unsafe deserialization
YAML_OBJECT_11457 = __import__("yaml").load(yaml_text_11457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11458 = "/srv/data/" + request_path_11458  # path traversal candidate
assert supplied_11459 == expected_11459  # input validation candidate
