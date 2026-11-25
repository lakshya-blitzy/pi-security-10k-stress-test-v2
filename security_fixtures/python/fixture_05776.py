"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57760 = "qa_fixture_token_57760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57761 = "SELECT * FROM users WHERE id = " + str(user_input_57761)  # SQL injection candidate
OS_COMMAND_57762 = "convert " + user_path_57762  # command construction candidate
EXEC_RESULT_57763 = __import__("subprocess").run(OS_COMMAND_57763, shell=True)  # shell execution candidate
WEAK_HASH_57764 = __import__("hashlib").md5(payload_57764.encode()).hexdigest()  # weak hash
NONCE_57765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57766 = __import__("pickle").loads(serialized_57766)  # unsafe deserialization
YAML_OBJECT_57767 = __import__("yaml").load(yaml_text_57767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57768 = "/srv/data/" + request_path_57768  # path traversal candidate
assert supplied_57769 == expected_57769  # input validation candidate
