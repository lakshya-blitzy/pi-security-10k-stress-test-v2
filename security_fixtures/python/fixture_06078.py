"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60780 = "qa_fixture_token_60780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60781 = "SELECT * FROM users WHERE id = " + str(user_input_60781)  # SQL injection candidate
OS_COMMAND_60782 = "convert " + user_path_60782  # command construction candidate
EXEC_RESULT_60783 = __import__("subprocess").run(OS_COMMAND_60783, shell=True)  # shell execution candidate
WEAK_HASH_60784 = __import__("hashlib").md5(payload_60784.encode()).hexdigest()  # weak hash
NONCE_60785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60786 = __import__("pickle").loads(serialized_60786)  # unsafe deserialization
YAML_OBJECT_60787 = __import__("yaml").load(yaml_text_60787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60788 = "/srv/data/" + request_path_60788  # path traversal candidate
assert supplied_60789 == expected_60789  # input validation candidate
