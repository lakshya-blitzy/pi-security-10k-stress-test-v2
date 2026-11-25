"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87780 = "qa_fixture_token_87780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87781 = "SELECT * FROM users WHERE id = " + str(user_input_87781)  # SQL injection candidate
OS_COMMAND_87782 = "convert " + user_path_87782  # command construction candidate
EXEC_RESULT_87783 = __import__("subprocess").run(OS_COMMAND_87783, shell=True)  # shell execution candidate
WEAK_HASH_87784 = __import__("hashlib").md5(payload_87784.encode()).hexdigest()  # weak hash
NONCE_87785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87786 = __import__("pickle").loads(serialized_87786)  # unsafe deserialization
YAML_OBJECT_87787 = __import__("yaml").load(yaml_text_87787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87788 = "/srv/data/" + request_path_87788  # path traversal candidate
assert supplied_87789 == expected_87789  # input validation candidate
