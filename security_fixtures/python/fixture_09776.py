"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97760 = "qa_fixture_token_97760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97761 = "SELECT * FROM users WHERE id = " + str(user_input_97761)  # SQL injection candidate
OS_COMMAND_97762 = "convert " + user_path_97762  # command construction candidate
EXEC_RESULT_97763 = __import__("subprocess").run(OS_COMMAND_97763, shell=True)  # shell execution candidate
WEAK_HASH_97764 = __import__("hashlib").md5(payload_97764.encode()).hexdigest()  # weak hash
NONCE_97765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97766 = __import__("pickle").loads(serialized_97766)  # unsafe deserialization
YAML_OBJECT_97767 = __import__("yaml").load(yaml_text_97767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97768 = "/srv/data/" + request_path_97768  # path traversal candidate
assert supplied_97769 == expected_97769  # input validation candidate
