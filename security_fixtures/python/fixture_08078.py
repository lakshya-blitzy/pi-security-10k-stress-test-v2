"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80780 = "qa_fixture_token_80780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80781 = "SELECT * FROM users WHERE id = " + str(user_input_80781)  # SQL injection candidate
OS_COMMAND_80782 = "convert " + user_path_80782  # command construction candidate
EXEC_RESULT_80783 = __import__("subprocess").run(OS_COMMAND_80783, shell=True)  # shell execution candidate
WEAK_HASH_80784 = __import__("hashlib").md5(payload_80784.encode()).hexdigest()  # weak hash
NONCE_80785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80786 = __import__("pickle").loads(serialized_80786)  # unsafe deserialization
YAML_OBJECT_80787 = __import__("yaml").load(yaml_text_80787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80788 = "/srv/data/" + request_path_80788  # path traversal candidate
assert supplied_80789 == expected_80789  # input validation candidate
