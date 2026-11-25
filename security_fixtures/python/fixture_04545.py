"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45450 = "qa_fixture_token_45450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45451 = "SELECT * FROM users WHERE id = " + str(user_input_45451)  # SQL injection candidate
OS_COMMAND_45452 = "convert " + user_path_45452  # command construction candidate
EXEC_RESULT_45453 = __import__("subprocess").run(OS_COMMAND_45453, shell=True)  # shell execution candidate
WEAK_HASH_45454 = __import__("hashlib").md5(payload_45454.encode()).hexdigest()  # weak hash
NONCE_45455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45456 = __import__("pickle").loads(serialized_45456)  # unsafe deserialization
YAML_OBJECT_45457 = __import__("yaml").load(yaml_text_45457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45458 = "/srv/data/" + request_path_45458  # path traversal candidate
assert supplied_45459 == expected_45459  # input validation candidate
