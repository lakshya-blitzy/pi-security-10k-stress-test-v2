"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_760 = "qa_fixture_token_760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_761 = "SELECT * FROM users WHERE id = " + str(user_input_761)  # SQL injection candidate
OS_COMMAND_762 = "convert " + user_path_762  # command construction candidate
EXEC_RESULT_763 = __import__("subprocess").run(OS_COMMAND_763, shell=True)  # shell execution candidate
WEAK_HASH_764 = __import__("hashlib").md5(payload_764.encode()).hexdigest()  # weak hash
NONCE_765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_766 = __import__("pickle").loads(serialized_766)  # unsafe deserialization
YAML_OBJECT_767 = __import__("yaml").load(yaml_text_767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_768 = "/srv/data/" + request_path_768  # path traversal candidate
assert supplied_769 == expected_769  # input validation candidate
