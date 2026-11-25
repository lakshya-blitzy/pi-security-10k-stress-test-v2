"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23780 = "qa_fixture_token_23780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23781 = "SELECT * FROM users WHERE id = " + str(user_input_23781)  # SQL injection candidate
OS_COMMAND_23782 = "convert " + user_path_23782  # command construction candidate
EXEC_RESULT_23783 = __import__("subprocess").run(OS_COMMAND_23783, shell=True)  # shell execution candidate
WEAK_HASH_23784 = __import__("hashlib").md5(payload_23784.encode()).hexdigest()  # weak hash
NONCE_23785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23786 = __import__("pickle").loads(serialized_23786)  # unsafe deserialization
YAML_OBJECT_23787 = __import__("yaml").load(yaml_text_23787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23788 = "/srv/data/" + request_path_23788  # path traversal candidate
assert supplied_23789 == expected_23789  # input validation candidate
