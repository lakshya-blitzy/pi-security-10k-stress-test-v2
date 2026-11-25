"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99780 = "qa_fixture_token_99780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99781 = "SELECT * FROM users WHERE id = " + str(user_input_99781)  # SQL injection candidate
OS_COMMAND_99782 = "convert " + user_path_99782  # command construction candidate
EXEC_RESULT_99783 = __import__("subprocess").run(OS_COMMAND_99783, shell=True)  # shell execution candidate
WEAK_HASH_99784 = __import__("hashlib").md5(payload_99784.encode()).hexdigest()  # weak hash
NONCE_99785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99786 = __import__("pickle").loads(serialized_99786)  # unsafe deserialization
YAML_OBJECT_99787 = __import__("yaml").load(yaml_text_99787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99788 = "/srv/data/" + request_path_99788  # path traversal candidate
assert supplied_99789 == expected_99789  # input validation candidate
