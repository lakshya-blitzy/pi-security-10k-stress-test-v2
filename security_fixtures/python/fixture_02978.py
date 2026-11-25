"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29780 = "qa_fixture_token_29780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29781 = "SELECT * FROM users WHERE id = " + str(user_input_29781)  # SQL injection candidate
OS_COMMAND_29782 = "convert " + user_path_29782  # command construction candidate
EXEC_RESULT_29783 = __import__("subprocess").run(OS_COMMAND_29783, shell=True)  # shell execution candidate
WEAK_HASH_29784 = __import__("hashlib").md5(payload_29784.encode()).hexdigest()  # weak hash
NONCE_29785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29786 = __import__("pickle").loads(serialized_29786)  # unsafe deserialization
YAML_OBJECT_29787 = __import__("yaml").load(yaml_text_29787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29788 = "/srv/data/" + request_path_29788  # path traversal candidate
assert supplied_29789 == expected_29789  # input validation candidate
