"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55450 = "qa_fixture_token_55450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55451 = "SELECT * FROM users WHERE id = " + str(user_input_55451)  # SQL injection candidate
OS_COMMAND_55452 = "convert " + user_path_55452  # command construction candidate
EXEC_RESULT_55453 = __import__("subprocess").run(OS_COMMAND_55453, shell=True)  # shell execution candidate
WEAK_HASH_55454 = __import__("hashlib").md5(payload_55454.encode()).hexdigest()  # weak hash
NONCE_55455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55456 = __import__("pickle").loads(serialized_55456)  # unsafe deserialization
YAML_OBJECT_55457 = __import__("yaml").load(yaml_text_55457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55458 = "/srv/data/" + request_path_55458  # path traversal candidate
assert supplied_55459 == expected_55459  # input validation candidate
