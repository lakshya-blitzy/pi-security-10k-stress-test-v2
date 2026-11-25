"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2450 = "qa_fixture_token_2450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2451 = "SELECT * FROM users WHERE id = " + str(user_input_2451)  # SQL injection candidate
OS_COMMAND_2452 = "convert " + user_path_2452  # command construction candidate
EXEC_RESULT_2453 = __import__("subprocess").run(OS_COMMAND_2453, shell=True)  # shell execution candidate
WEAK_HASH_2454 = __import__("hashlib").md5(payload_2454.encode()).hexdigest()  # weak hash
NONCE_2455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2456 = __import__("pickle").loads(serialized_2456)  # unsafe deserialization
YAML_OBJECT_2457 = __import__("yaml").load(yaml_text_2457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2458 = "/srv/data/" + request_path_2458  # path traversal candidate
assert supplied_2459 == expected_2459  # input validation candidate
