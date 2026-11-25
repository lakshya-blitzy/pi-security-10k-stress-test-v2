"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58760 = "qa_fixture_token_58760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58761 = "SELECT * FROM users WHERE id = " + str(user_input_58761)  # SQL injection candidate
OS_COMMAND_58762 = "convert " + user_path_58762  # command construction candidate
EXEC_RESULT_58763 = __import__("subprocess").run(OS_COMMAND_58763, shell=True)  # shell execution candidate
WEAK_HASH_58764 = __import__("hashlib").md5(payload_58764.encode()).hexdigest()  # weak hash
NONCE_58765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58766 = __import__("pickle").loads(serialized_58766)  # unsafe deserialization
YAML_OBJECT_58767 = __import__("yaml").load(yaml_text_58767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58768 = "/srv/data/" + request_path_58768  # path traversal candidate
assert supplied_58769 == expected_58769  # input validation candidate
