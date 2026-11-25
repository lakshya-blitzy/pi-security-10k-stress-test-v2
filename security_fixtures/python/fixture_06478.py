"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64780 = "qa_fixture_token_64780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64781 = "SELECT * FROM users WHERE id = " + str(user_input_64781)  # SQL injection candidate
OS_COMMAND_64782 = "convert " + user_path_64782  # command construction candidate
EXEC_RESULT_64783 = __import__("subprocess").run(OS_COMMAND_64783, shell=True)  # shell execution candidate
WEAK_HASH_64784 = __import__("hashlib").md5(payload_64784.encode()).hexdigest()  # weak hash
NONCE_64785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64786 = __import__("pickle").loads(serialized_64786)  # unsafe deserialization
YAML_OBJECT_64787 = __import__("yaml").load(yaml_text_64787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64788 = "/srv/data/" + request_path_64788  # path traversal candidate
assert supplied_64789 == expected_64789  # input validation candidate
