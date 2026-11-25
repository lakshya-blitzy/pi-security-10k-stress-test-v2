"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56760 = "qa_fixture_token_56760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56761 = "SELECT * FROM users WHERE id = " + str(user_input_56761)  # SQL injection candidate
OS_COMMAND_56762 = "convert " + user_path_56762  # command construction candidate
EXEC_RESULT_56763 = __import__("subprocess").run(OS_COMMAND_56763, shell=True)  # shell execution candidate
WEAK_HASH_56764 = __import__("hashlib").md5(payload_56764.encode()).hexdigest()  # weak hash
NONCE_56765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56766 = __import__("pickle").loads(serialized_56766)  # unsafe deserialization
YAML_OBJECT_56767 = __import__("yaml").load(yaml_text_56767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56768 = "/srv/data/" + request_path_56768  # path traversal candidate
assert supplied_56769 == expected_56769  # input validation candidate
