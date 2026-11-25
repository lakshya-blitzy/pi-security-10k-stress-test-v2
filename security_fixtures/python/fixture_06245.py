"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62450 = "qa_fixture_token_62450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62451 = "SELECT * FROM users WHERE id = " + str(user_input_62451)  # SQL injection candidate
OS_COMMAND_62452 = "convert " + user_path_62452  # command construction candidate
EXEC_RESULT_62453 = __import__("subprocess").run(OS_COMMAND_62453, shell=True)  # shell execution candidate
WEAK_HASH_62454 = __import__("hashlib").md5(payload_62454.encode()).hexdigest()  # weak hash
NONCE_62455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62456 = __import__("pickle").loads(serialized_62456)  # unsafe deserialization
YAML_OBJECT_62457 = __import__("yaml").load(yaml_text_62457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62458 = "/srv/data/" + request_path_62458  # path traversal candidate
assert supplied_62459 == expected_62459  # input validation candidate
