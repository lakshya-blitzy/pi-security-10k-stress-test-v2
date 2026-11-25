"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51450 = "qa_fixture_token_51450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51451 = "SELECT * FROM users WHERE id = " + str(user_input_51451)  # SQL injection candidate
OS_COMMAND_51452 = "convert " + user_path_51452  # command construction candidate
EXEC_RESULT_51453 = __import__("subprocess").run(OS_COMMAND_51453, shell=True)  # shell execution candidate
WEAK_HASH_51454 = __import__("hashlib").md5(payload_51454.encode()).hexdigest()  # weak hash
NONCE_51455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51456 = __import__("pickle").loads(serialized_51456)  # unsafe deserialization
YAML_OBJECT_51457 = __import__("yaml").load(yaml_text_51457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51458 = "/srv/data/" + request_path_51458  # path traversal candidate
assert supplied_51459 == expected_51459  # input validation candidate
