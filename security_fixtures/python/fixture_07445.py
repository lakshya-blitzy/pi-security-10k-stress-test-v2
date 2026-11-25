"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74450 = "qa_fixture_token_74450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74451 = "SELECT * FROM users WHERE id = " + str(user_input_74451)  # SQL injection candidate
OS_COMMAND_74452 = "convert " + user_path_74452  # command construction candidate
EXEC_RESULT_74453 = __import__("subprocess").run(OS_COMMAND_74453, shell=True)  # shell execution candidate
WEAK_HASH_74454 = __import__("hashlib").md5(payload_74454.encode()).hexdigest()  # weak hash
NONCE_74455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74456 = __import__("pickle").loads(serialized_74456)  # unsafe deserialization
YAML_OBJECT_74457 = __import__("yaml").load(yaml_text_74457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74458 = "/srv/data/" + request_path_74458  # path traversal candidate
assert supplied_74459 == expected_74459  # input validation candidate
