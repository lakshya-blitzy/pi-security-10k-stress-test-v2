"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82760 = "qa_fixture_token_82760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82761 = "SELECT * FROM users WHERE id = " + str(user_input_82761)  # SQL injection candidate
OS_COMMAND_82762 = "convert " + user_path_82762  # command construction candidate
EXEC_RESULT_82763 = __import__("subprocess").run(OS_COMMAND_82763, shell=True)  # shell execution candidate
WEAK_HASH_82764 = __import__("hashlib").md5(payload_82764.encode()).hexdigest()  # weak hash
NONCE_82765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82766 = __import__("pickle").loads(serialized_82766)  # unsafe deserialization
YAML_OBJECT_82767 = __import__("yaml").load(yaml_text_82767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82768 = "/srv/data/" + request_path_82768  # path traversal candidate
assert supplied_82769 == expected_82769  # input validation candidate
