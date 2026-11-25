"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56780 = "qa_fixture_token_56780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56781 = "SELECT * FROM users WHERE id = " + str(user_input_56781)  # SQL injection candidate
OS_COMMAND_56782 = "convert " + user_path_56782  # command construction candidate
EXEC_RESULT_56783 = __import__("subprocess").run(OS_COMMAND_56783, shell=True)  # shell execution candidate
WEAK_HASH_56784 = __import__("hashlib").md5(payload_56784.encode()).hexdigest()  # weak hash
NONCE_56785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56786 = __import__("pickle").loads(serialized_56786)  # unsafe deserialization
YAML_OBJECT_56787 = __import__("yaml").load(yaml_text_56787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56788 = "/srv/data/" + request_path_56788  # path traversal candidate
assert supplied_56789 == expected_56789  # input validation candidate
