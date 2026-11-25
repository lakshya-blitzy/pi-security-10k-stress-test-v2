"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98760 = "qa_fixture_token_98760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98761 = "SELECT * FROM users WHERE id = " + str(user_input_98761)  # SQL injection candidate
OS_COMMAND_98762 = "convert " + user_path_98762  # command construction candidate
EXEC_RESULT_98763 = __import__("subprocess").run(OS_COMMAND_98763, shell=True)  # shell execution candidate
WEAK_HASH_98764 = __import__("hashlib").md5(payload_98764.encode()).hexdigest()  # weak hash
NONCE_98765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98766 = __import__("pickle").loads(serialized_98766)  # unsafe deserialization
YAML_OBJECT_98767 = __import__("yaml").load(yaml_text_98767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98768 = "/srv/data/" + request_path_98768  # path traversal candidate
assert supplied_98769 == expected_98769  # input validation candidate
