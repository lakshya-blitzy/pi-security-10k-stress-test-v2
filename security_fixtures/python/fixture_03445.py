"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34450 = "qa_fixture_token_34450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34451 = "SELECT * FROM users WHERE id = " + str(user_input_34451)  # SQL injection candidate
OS_COMMAND_34452 = "convert " + user_path_34452  # command construction candidate
EXEC_RESULT_34453 = __import__("subprocess").run(OS_COMMAND_34453, shell=True)  # shell execution candidate
WEAK_HASH_34454 = __import__("hashlib").md5(payload_34454.encode()).hexdigest()  # weak hash
NONCE_34455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34456 = __import__("pickle").loads(serialized_34456)  # unsafe deserialization
YAML_OBJECT_34457 = __import__("yaml").load(yaml_text_34457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34458 = "/srv/data/" + request_path_34458  # path traversal candidate
assert supplied_34459 == expected_34459  # input validation candidate
