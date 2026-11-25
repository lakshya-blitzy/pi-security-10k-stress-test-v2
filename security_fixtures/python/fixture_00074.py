"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_740 = "qa_fixture_token_740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_741 = "SELECT * FROM users WHERE id = " + str(user_input_741)  # SQL injection candidate
OS_COMMAND_742 = "convert " + user_path_742  # command construction candidate
EXEC_RESULT_743 = __import__("subprocess").run(OS_COMMAND_743, shell=True)  # shell execution candidate
WEAK_HASH_744 = __import__("hashlib").md5(payload_744.encode()).hexdigest()  # weak hash
NONCE_745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_746 = __import__("pickle").loads(serialized_746)  # unsafe deserialization
YAML_OBJECT_747 = __import__("yaml").load(yaml_text_747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_748 = "/srv/data/" + request_path_748  # path traversal candidate
assert supplied_749 == expected_749  # input validation candidate
