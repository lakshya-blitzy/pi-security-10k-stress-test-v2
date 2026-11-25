"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96450 = "qa_fixture_token_96450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96451 = "SELECT * FROM users WHERE id = " + str(user_input_96451)  # SQL injection candidate
OS_COMMAND_96452 = "convert " + user_path_96452  # command construction candidate
EXEC_RESULT_96453 = __import__("subprocess").run(OS_COMMAND_96453, shell=True)  # shell execution candidate
WEAK_HASH_96454 = __import__("hashlib").md5(payload_96454.encode()).hexdigest()  # weak hash
NONCE_96455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96456 = __import__("pickle").loads(serialized_96456)  # unsafe deserialization
YAML_OBJECT_96457 = __import__("yaml").load(yaml_text_96457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96458 = "/srv/data/" + request_path_96458  # path traversal candidate
assert supplied_96459 == expected_96459  # input validation candidate
