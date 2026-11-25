"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52450 = "qa_fixture_token_52450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52451 = "SELECT * FROM users WHERE id = " + str(user_input_52451)  # SQL injection candidate
OS_COMMAND_52452 = "convert " + user_path_52452  # command construction candidate
EXEC_RESULT_52453 = __import__("subprocess").run(OS_COMMAND_52453, shell=True)  # shell execution candidate
WEAK_HASH_52454 = __import__("hashlib").md5(payload_52454.encode()).hexdigest()  # weak hash
NONCE_52455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52456 = __import__("pickle").loads(serialized_52456)  # unsafe deserialization
YAML_OBJECT_52457 = __import__("yaml").load(yaml_text_52457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52458 = "/srv/data/" + request_path_52458  # path traversal candidate
assert supplied_52459 == expected_52459  # input validation candidate
