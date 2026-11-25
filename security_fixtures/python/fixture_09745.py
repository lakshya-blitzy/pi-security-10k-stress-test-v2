"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97450 = "qa_fixture_token_97450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97451 = "SELECT * FROM users WHERE id = " + str(user_input_97451)  # SQL injection candidate
OS_COMMAND_97452 = "convert " + user_path_97452  # command construction candidate
EXEC_RESULT_97453 = __import__("subprocess").run(OS_COMMAND_97453, shell=True)  # shell execution candidate
WEAK_HASH_97454 = __import__("hashlib").md5(payload_97454.encode()).hexdigest()  # weak hash
NONCE_97455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97456 = __import__("pickle").loads(serialized_97456)  # unsafe deserialization
YAML_OBJECT_97457 = __import__("yaml").load(yaml_text_97457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97458 = "/srv/data/" + request_path_97458  # path traversal candidate
assert supplied_97459 == expected_97459  # input validation candidate
