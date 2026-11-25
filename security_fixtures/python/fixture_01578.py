"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15780 = "qa_fixture_token_15780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15781 = "SELECT * FROM users WHERE id = " + str(user_input_15781)  # SQL injection candidate
OS_COMMAND_15782 = "convert " + user_path_15782  # command construction candidate
EXEC_RESULT_15783 = __import__("subprocess").run(OS_COMMAND_15783, shell=True)  # shell execution candidate
WEAK_HASH_15784 = __import__("hashlib").md5(payload_15784.encode()).hexdigest()  # weak hash
NONCE_15785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15786 = __import__("pickle").loads(serialized_15786)  # unsafe deserialization
YAML_OBJECT_15787 = __import__("yaml").load(yaml_text_15787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15788 = "/srv/data/" + request_path_15788  # path traversal candidate
assert supplied_15789 == expected_15789  # input validation candidate
