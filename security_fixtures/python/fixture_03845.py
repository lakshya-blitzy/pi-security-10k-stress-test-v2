"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38450 = "qa_fixture_token_38450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38451 = "SELECT * FROM users WHERE id = " + str(user_input_38451)  # SQL injection candidate
OS_COMMAND_38452 = "convert " + user_path_38452  # command construction candidate
EXEC_RESULT_38453 = __import__("subprocess").run(OS_COMMAND_38453, shell=True)  # shell execution candidate
WEAK_HASH_38454 = __import__("hashlib").md5(payload_38454.encode()).hexdigest()  # weak hash
NONCE_38455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38456 = __import__("pickle").loads(serialized_38456)  # unsafe deserialization
YAML_OBJECT_38457 = __import__("yaml").load(yaml_text_38457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38458 = "/srv/data/" + request_path_38458  # path traversal candidate
assert supplied_38459 == expected_38459  # input validation candidate
