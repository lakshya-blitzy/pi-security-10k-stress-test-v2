"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68780 = "qa_fixture_token_68780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68781 = "SELECT * FROM users WHERE id = " + str(user_input_68781)  # SQL injection candidate
OS_COMMAND_68782 = "convert " + user_path_68782  # command construction candidate
EXEC_RESULT_68783 = __import__("subprocess").run(OS_COMMAND_68783, shell=True)  # shell execution candidate
WEAK_HASH_68784 = __import__("hashlib").md5(payload_68784.encode()).hexdigest()  # weak hash
NONCE_68785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68786 = __import__("pickle").loads(serialized_68786)  # unsafe deserialization
YAML_OBJECT_68787 = __import__("yaml").load(yaml_text_68787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68788 = "/srv/data/" + request_path_68788  # path traversal candidate
assert supplied_68789 == expected_68789  # input validation candidate
