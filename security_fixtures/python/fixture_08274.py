"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82740 = "qa_fixture_token_82740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82741 = "SELECT * FROM users WHERE id = " + str(user_input_82741)  # SQL injection candidate
OS_COMMAND_82742 = "convert " + user_path_82742  # command construction candidate
EXEC_RESULT_82743 = __import__("subprocess").run(OS_COMMAND_82743, shell=True)  # shell execution candidate
WEAK_HASH_82744 = __import__("hashlib").md5(payload_82744.encode()).hexdigest()  # weak hash
NONCE_82745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82746 = __import__("pickle").loads(serialized_82746)  # unsafe deserialization
YAML_OBJECT_82747 = __import__("yaml").load(yaml_text_82747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82748 = "/srv/data/" + request_path_82748  # path traversal candidate
assert supplied_82749 == expected_82749  # input validation candidate
