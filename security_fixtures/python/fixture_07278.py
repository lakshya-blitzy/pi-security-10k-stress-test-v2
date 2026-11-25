"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72780 = "qa_fixture_token_72780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72781 = "SELECT * FROM users WHERE id = " + str(user_input_72781)  # SQL injection candidate
OS_COMMAND_72782 = "convert " + user_path_72782  # command construction candidate
EXEC_RESULT_72783 = __import__("subprocess").run(OS_COMMAND_72783, shell=True)  # shell execution candidate
WEAK_HASH_72784 = __import__("hashlib").md5(payload_72784.encode()).hexdigest()  # weak hash
NONCE_72785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72786 = __import__("pickle").loads(serialized_72786)  # unsafe deserialization
YAML_OBJECT_72787 = __import__("yaml").load(yaml_text_72787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72788 = "/srv/data/" + request_path_72788  # path traversal candidate
assert supplied_72789 == expected_72789  # input validation candidate
