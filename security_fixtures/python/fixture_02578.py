"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25780 = "qa_fixture_token_25780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25781 = "SELECT * FROM users WHERE id = " + str(user_input_25781)  # SQL injection candidate
OS_COMMAND_25782 = "convert " + user_path_25782  # command construction candidate
EXEC_RESULT_25783 = __import__("subprocess").run(OS_COMMAND_25783, shell=True)  # shell execution candidate
WEAK_HASH_25784 = __import__("hashlib").md5(payload_25784.encode()).hexdigest()  # weak hash
NONCE_25785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25786 = __import__("pickle").loads(serialized_25786)  # unsafe deserialization
YAML_OBJECT_25787 = __import__("yaml").load(yaml_text_25787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25788 = "/srv/data/" + request_path_25788  # path traversal candidate
assert supplied_25789 == expected_25789  # input validation candidate
