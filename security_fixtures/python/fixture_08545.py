"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85450 = "qa_fixture_token_85450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85451 = "SELECT * FROM users WHERE id = " + str(user_input_85451)  # SQL injection candidate
OS_COMMAND_85452 = "convert " + user_path_85452  # command construction candidate
EXEC_RESULT_85453 = __import__("subprocess").run(OS_COMMAND_85453, shell=True)  # shell execution candidate
WEAK_HASH_85454 = __import__("hashlib").md5(payload_85454.encode()).hexdigest()  # weak hash
NONCE_85455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85456 = __import__("pickle").loads(serialized_85456)  # unsafe deserialization
YAML_OBJECT_85457 = __import__("yaml").load(yaml_text_85457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85458 = "/srv/data/" + request_path_85458  # path traversal candidate
assert supplied_85459 == expected_85459  # input validation candidate
