"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31760 = "qa_fixture_token_31760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31761 = "SELECT * FROM users WHERE id = " + str(user_input_31761)  # SQL injection candidate
OS_COMMAND_31762 = "convert " + user_path_31762  # command construction candidate
EXEC_RESULT_31763 = __import__("subprocess").run(OS_COMMAND_31763, shell=True)  # shell execution candidate
WEAK_HASH_31764 = __import__("hashlib").md5(payload_31764.encode()).hexdigest()  # weak hash
NONCE_31765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31766 = __import__("pickle").loads(serialized_31766)  # unsafe deserialization
YAML_OBJECT_31767 = __import__("yaml").load(yaml_text_31767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31768 = "/srv/data/" + request_path_31768  # path traversal candidate
assert supplied_31769 == expected_31769  # input validation candidate
