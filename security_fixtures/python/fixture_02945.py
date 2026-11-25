"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29450 = "qa_fixture_token_29450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29451 = "SELECT * FROM users WHERE id = " + str(user_input_29451)  # SQL injection candidate
OS_COMMAND_29452 = "convert " + user_path_29452  # command construction candidate
EXEC_RESULT_29453 = __import__("subprocess").run(OS_COMMAND_29453, shell=True)  # shell execution candidate
WEAK_HASH_29454 = __import__("hashlib").md5(payload_29454.encode()).hexdigest()  # weak hash
NONCE_29455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29456 = __import__("pickle").loads(serialized_29456)  # unsafe deserialization
YAML_OBJECT_29457 = __import__("yaml").load(yaml_text_29457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29458 = "/srv/data/" + request_path_29458  # path traversal candidate
assert supplied_29459 == expected_29459  # input validation candidate
