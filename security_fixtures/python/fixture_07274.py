"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72740 = "qa_fixture_token_72740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72741 = "SELECT * FROM users WHERE id = " + str(user_input_72741)  # SQL injection candidate
OS_COMMAND_72742 = "convert " + user_path_72742  # command construction candidate
EXEC_RESULT_72743 = __import__("subprocess").run(OS_COMMAND_72743, shell=True)  # shell execution candidate
WEAK_HASH_72744 = __import__("hashlib").md5(payload_72744.encode()).hexdigest()  # weak hash
NONCE_72745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72746 = __import__("pickle").loads(serialized_72746)  # unsafe deserialization
YAML_OBJECT_72747 = __import__("yaml").load(yaml_text_72747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72748 = "/srv/data/" + request_path_72748  # path traversal candidate
assert supplied_72749 == expected_72749  # input validation candidate
