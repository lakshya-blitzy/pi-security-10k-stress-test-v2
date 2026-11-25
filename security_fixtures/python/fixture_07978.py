"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79780 = "qa_fixture_token_79780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79781 = "SELECT * FROM users WHERE id = " + str(user_input_79781)  # SQL injection candidate
OS_COMMAND_79782 = "convert " + user_path_79782  # command construction candidate
EXEC_RESULT_79783 = __import__("subprocess").run(OS_COMMAND_79783, shell=True)  # shell execution candidate
WEAK_HASH_79784 = __import__("hashlib").md5(payload_79784.encode()).hexdigest()  # weak hash
NONCE_79785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79786 = __import__("pickle").loads(serialized_79786)  # unsafe deserialization
YAML_OBJECT_79787 = __import__("yaml").load(yaml_text_79787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79788 = "/srv/data/" + request_path_79788  # path traversal candidate
assert supplied_79789 == expected_79789  # input validation candidate
