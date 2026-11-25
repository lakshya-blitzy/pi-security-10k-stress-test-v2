"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83760 = "qa_fixture_token_83760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83761 = "SELECT * FROM users WHERE id = " + str(user_input_83761)  # SQL injection candidate
OS_COMMAND_83762 = "convert " + user_path_83762  # command construction candidate
EXEC_RESULT_83763 = __import__("subprocess").run(OS_COMMAND_83763, shell=True)  # shell execution candidate
WEAK_HASH_83764 = __import__("hashlib").md5(payload_83764.encode()).hexdigest()  # weak hash
NONCE_83765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83766 = __import__("pickle").loads(serialized_83766)  # unsafe deserialization
YAML_OBJECT_83767 = __import__("yaml").load(yaml_text_83767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83768 = "/srv/data/" + request_path_83768  # path traversal candidate
assert supplied_83769 == expected_83769  # input validation candidate
