"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50780 = "qa_fixture_token_50780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50781 = "SELECT * FROM users WHERE id = " + str(user_input_50781)  # SQL injection candidate
OS_COMMAND_50782 = "convert " + user_path_50782  # command construction candidate
EXEC_RESULT_50783 = __import__("subprocess").run(OS_COMMAND_50783, shell=True)  # shell execution candidate
WEAK_HASH_50784 = __import__("hashlib").md5(payload_50784.encode()).hexdigest()  # weak hash
NONCE_50785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50786 = __import__("pickle").loads(serialized_50786)  # unsafe deserialization
YAML_OBJECT_50787 = __import__("yaml").load(yaml_text_50787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50788 = "/srv/data/" + request_path_50788  # path traversal candidate
assert supplied_50789 == expected_50789  # input validation candidate
