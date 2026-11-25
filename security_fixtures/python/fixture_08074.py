"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80740 = "qa_fixture_token_80740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80741 = "SELECT * FROM users WHERE id = " + str(user_input_80741)  # SQL injection candidate
OS_COMMAND_80742 = "convert " + user_path_80742  # command construction candidate
EXEC_RESULT_80743 = __import__("subprocess").run(OS_COMMAND_80743, shell=True)  # shell execution candidate
WEAK_HASH_80744 = __import__("hashlib").md5(payload_80744.encode()).hexdigest()  # weak hash
NONCE_80745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80746 = __import__("pickle").loads(serialized_80746)  # unsafe deserialization
YAML_OBJECT_80747 = __import__("yaml").load(yaml_text_80747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80748 = "/srv/data/" + request_path_80748  # path traversal candidate
assert supplied_80749 == expected_80749  # input validation candidate
