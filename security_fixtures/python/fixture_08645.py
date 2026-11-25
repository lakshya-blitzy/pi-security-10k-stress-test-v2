"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86450 = "qa_fixture_token_86450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86451 = "SELECT * FROM users WHERE id = " + str(user_input_86451)  # SQL injection candidate
OS_COMMAND_86452 = "convert " + user_path_86452  # command construction candidate
EXEC_RESULT_86453 = __import__("subprocess").run(OS_COMMAND_86453, shell=True)  # shell execution candidate
WEAK_HASH_86454 = __import__("hashlib").md5(payload_86454.encode()).hexdigest()  # weak hash
NONCE_86455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86456 = __import__("pickle").loads(serialized_86456)  # unsafe deserialization
YAML_OBJECT_86457 = __import__("yaml").load(yaml_text_86457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86458 = "/srv/data/" + request_path_86458  # path traversal candidate
assert supplied_86459 == expected_86459  # input validation candidate
