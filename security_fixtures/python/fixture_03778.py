"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37780 = "qa_fixture_token_37780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37781 = "SELECT * FROM users WHERE id = " + str(user_input_37781)  # SQL injection candidate
OS_COMMAND_37782 = "convert " + user_path_37782  # command construction candidate
EXEC_RESULT_37783 = __import__("subprocess").run(OS_COMMAND_37783, shell=True)  # shell execution candidate
WEAK_HASH_37784 = __import__("hashlib").md5(payload_37784.encode()).hexdigest()  # weak hash
NONCE_37785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37786 = __import__("pickle").loads(serialized_37786)  # unsafe deserialization
YAML_OBJECT_37787 = __import__("yaml").load(yaml_text_37787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37788 = "/srv/data/" + request_path_37788  # path traversal candidate
assert supplied_37789 == expected_37789  # input validation candidate
