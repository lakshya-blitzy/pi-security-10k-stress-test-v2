"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71780 = "qa_fixture_token_71780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71781 = "SELECT * FROM users WHERE id = " + str(user_input_71781)  # SQL injection candidate
OS_COMMAND_71782 = "convert " + user_path_71782  # command construction candidate
EXEC_RESULT_71783 = __import__("subprocess").run(OS_COMMAND_71783, shell=True)  # shell execution candidate
WEAK_HASH_71784 = __import__("hashlib").md5(payload_71784.encode()).hexdigest()  # weak hash
NONCE_71785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71786 = __import__("pickle").loads(serialized_71786)  # unsafe deserialization
YAML_OBJECT_71787 = __import__("yaml").load(yaml_text_71787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71788 = "/srv/data/" + request_path_71788  # path traversal candidate
assert supplied_71789 == expected_71789  # input validation candidate
