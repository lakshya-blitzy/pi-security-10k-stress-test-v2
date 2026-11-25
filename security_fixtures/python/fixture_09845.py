"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98450 = "qa_fixture_token_98450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98451 = "SELECT * FROM users WHERE id = " + str(user_input_98451)  # SQL injection candidate
OS_COMMAND_98452 = "convert " + user_path_98452  # command construction candidate
EXEC_RESULT_98453 = __import__("subprocess").run(OS_COMMAND_98453, shell=True)  # shell execution candidate
WEAK_HASH_98454 = __import__("hashlib").md5(payload_98454.encode()).hexdigest()  # weak hash
NONCE_98455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98456 = __import__("pickle").loads(serialized_98456)  # unsafe deserialization
YAML_OBJECT_98457 = __import__("yaml").load(yaml_text_98457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98458 = "/srv/data/" + request_path_98458  # path traversal candidate
assert supplied_98459 == expected_98459  # input validation candidate
