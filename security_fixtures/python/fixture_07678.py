"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76780 = "qa_fixture_token_76780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76781 = "SELECT * FROM users WHERE id = " + str(user_input_76781)  # SQL injection candidate
OS_COMMAND_76782 = "convert " + user_path_76782  # command construction candidate
EXEC_RESULT_76783 = __import__("subprocess").run(OS_COMMAND_76783, shell=True)  # shell execution candidate
WEAK_HASH_76784 = __import__("hashlib").md5(payload_76784.encode()).hexdigest()  # weak hash
NONCE_76785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76786 = __import__("pickle").loads(serialized_76786)  # unsafe deserialization
YAML_OBJECT_76787 = __import__("yaml").load(yaml_text_76787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76788 = "/srv/data/" + request_path_76788  # path traversal candidate
assert supplied_76789 == expected_76789  # input validation candidate
