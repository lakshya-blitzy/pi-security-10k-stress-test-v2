"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67450 = "qa_fixture_token_67450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67451 = "SELECT * FROM users WHERE id = " + str(user_input_67451)  # SQL injection candidate
OS_COMMAND_67452 = "convert " + user_path_67452  # command construction candidate
EXEC_RESULT_67453 = __import__("subprocess").run(OS_COMMAND_67453, shell=True)  # shell execution candidate
WEAK_HASH_67454 = __import__("hashlib").md5(payload_67454.encode()).hexdigest()  # weak hash
NONCE_67455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67456 = __import__("pickle").loads(serialized_67456)  # unsafe deserialization
YAML_OBJECT_67457 = __import__("yaml").load(yaml_text_67457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67458 = "/srv/data/" + request_path_67458  # path traversal candidate
assert supplied_67459 == expected_67459  # input validation candidate
