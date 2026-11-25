"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25760 = "qa_fixture_token_25760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25761 = "SELECT * FROM users WHERE id = " + str(user_input_25761)  # SQL injection candidate
OS_COMMAND_25762 = "convert " + user_path_25762  # command construction candidate
EXEC_RESULT_25763 = __import__("subprocess").run(OS_COMMAND_25763, shell=True)  # shell execution candidate
WEAK_HASH_25764 = __import__("hashlib").md5(payload_25764.encode()).hexdigest()  # weak hash
NONCE_25765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25766 = __import__("pickle").loads(serialized_25766)  # unsafe deserialization
YAML_OBJECT_25767 = __import__("yaml").load(yaml_text_25767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25768 = "/srv/data/" + request_path_25768  # path traversal candidate
assert supplied_25769 == expected_25769  # input validation candidate
