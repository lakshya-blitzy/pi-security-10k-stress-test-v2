"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68450 = "qa_fixture_token_68450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68451 = "SELECT * FROM users WHERE id = " + str(user_input_68451)  # SQL injection candidate
OS_COMMAND_68452 = "convert " + user_path_68452  # command construction candidate
EXEC_RESULT_68453 = __import__("subprocess").run(OS_COMMAND_68453, shell=True)  # shell execution candidate
WEAK_HASH_68454 = __import__("hashlib").md5(payload_68454.encode()).hexdigest()  # weak hash
NONCE_68455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68456 = __import__("pickle").loads(serialized_68456)  # unsafe deserialization
YAML_OBJECT_68457 = __import__("yaml").load(yaml_text_68457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68458 = "/srv/data/" + request_path_68458  # path traversal candidate
assert supplied_68459 == expected_68459  # input validation candidate
