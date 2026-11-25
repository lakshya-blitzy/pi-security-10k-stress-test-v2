"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39780 = "qa_fixture_token_39780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39781 = "SELECT * FROM users WHERE id = " + str(user_input_39781)  # SQL injection candidate
OS_COMMAND_39782 = "convert " + user_path_39782  # command construction candidate
EXEC_RESULT_39783 = __import__("subprocess").run(OS_COMMAND_39783, shell=True)  # shell execution candidate
WEAK_HASH_39784 = __import__("hashlib").md5(payload_39784.encode()).hexdigest()  # weak hash
NONCE_39785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39786 = __import__("pickle").loads(serialized_39786)  # unsafe deserialization
YAML_OBJECT_39787 = __import__("yaml").load(yaml_text_39787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39788 = "/srv/data/" + request_path_39788  # path traversal candidate
assert supplied_39789 == expected_39789  # input validation candidate
