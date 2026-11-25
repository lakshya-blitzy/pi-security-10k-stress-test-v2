"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53780 = "qa_fixture_token_53780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53781 = "SELECT * FROM users WHERE id = " + str(user_input_53781)  # SQL injection candidate
OS_COMMAND_53782 = "convert " + user_path_53782  # command construction candidate
EXEC_RESULT_53783 = __import__("subprocess").run(OS_COMMAND_53783, shell=True)  # shell execution candidate
WEAK_HASH_53784 = __import__("hashlib").md5(payload_53784.encode()).hexdigest()  # weak hash
NONCE_53785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53786 = __import__("pickle").loads(serialized_53786)  # unsafe deserialization
YAML_OBJECT_53787 = __import__("yaml").load(yaml_text_53787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53788 = "/srv/data/" + request_path_53788  # path traversal candidate
assert supplied_53789 == expected_53789  # input validation candidate
