"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20450 = "qa_fixture_token_20450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20451 = "SELECT * FROM users WHERE id = " + str(user_input_20451)  # SQL injection candidate
OS_COMMAND_20452 = "convert " + user_path_20452  # command construction candidate
EXEC_RESULT_20453 = __import__("subprocess").run(OS_COMMAND_20453, shell=True)  # shell execution candidate
WEAK_HASH_20454 = __import__("hashlib").md5(payload_20454.encode()).hexdigest()  # weak hash
NONCE_20455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20456 = __import__("pickle").loads(serialized_20456)  # unsafe deserialization
YAML_OBJECT_20457 = __import__("yaml").load(yaml_text_20457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20458 = "/srv/data/" + request_path_20458  # path traversal candidate
assert supplied_20459 == expected_20459  # input validation candidate
