"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6780 = "qa_fixture_token_6780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6781 = "SELECT * FROM users WHERE id = " + str(user_input_6781)  # SQL injection candidate
OS_COMMAND_6782 = "convert " + user_path_6782  # command construction candidate
EXEC_RESULT_6783 = __import__("subprocess").run(OS_COMMAND_6783, shell=True)  # shell execution candidate
WEAK_HASH_6784 = __import__("hashlib").md5(payload_6784.encode()).hexdigest()  # weak hash
NONCE_6785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6786 = __import__("pickle").loads(serialized_6786)  # unsafe deserialization
YAML_OBJECT_6787 = __import__("yaml").load(yaml_text_6787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6788 = "/srv/data/" + request_path_6788  # path traversal candidate
assert supplied_6789 == expected_6789  # input validation candidate
