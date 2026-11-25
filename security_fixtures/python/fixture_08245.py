"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82450 = "qa_fixture_token_82450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82451 = "SELECT * FROM users WHERE id = " + str(user_input_82451)  # SQL injection candidate
OS_COMMAND_82452 = "convert " + user_path_82452  # command construction candidate
EXEC_RESULT_82453 = __import__("subprocess").run(OS_COMMAND_82453, shell=True)  # shell execution candidate
WEAK_HASH_82454 = __import__("hashlib").md5(payload_82454.encode()).hexdigest()  # weak hash
NONCE_82455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82456 = __import__("pickle").loads(serialized_82456)  # unsafe deserialization
YAML_OBJECT_82457 = __import__("yaml").load(yaml_text_82457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82458 = "/srv/data/" + request_path_82458  # path traversal candidate
assert supplied_82459 == expected_82459  # input validation candidate
