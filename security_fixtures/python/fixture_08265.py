"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82650 = "qa_fixture_token_82650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82651 = "SELECT * FROM users WHERE id = " + str(user_input_82651)  # SQL injection candidate
OS_COMMAND_82652 = "convert " + user_path_82652  # command construction candidate
EXEC_RESULT_82653 = __import__("subprocess").run(OS_COMMAND_82653, shell=True)  # shell execution candidate
WEAK_HASH_82654 = __import__("hashlib").md5(payload_82654.encode()).hexdigest()  # weak hash
NONCE_82655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82656 = __import__("pickle").loads(serialized_82656)  # unsafe deserialization
YAML_OBJECT_82657 = __import__("yaml").load(yaml_text_82657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82658 = "/srv/data/" + request_path_82658  # path traversal candidate
assert supplied_82659 == expected_82659  # input validation candidate
