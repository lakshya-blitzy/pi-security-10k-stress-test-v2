"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36780 = "qa_fixture_token_36780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36781 = "SELECT * FROM users WHERE id = " + str(user_input_36781)  # SQL injection candidate
OS_COMMAND_36782 = "convert " + user_path_36782  # command construction candidate
EXEC_RESULT_36783 = __import__("subprocess").run(OS_COMMAND_36783, shell=True)  # shell execution candidate
WEAK_HASH_36784 = __import__("hashlib").md5(payload_36784.encode()).hexdigest()  # weak hash
NONCE_36785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36786 = __import__("pickle").loads(serialized_36786)  # unsafe deserialization
YAML_OBJECT_36787 = __import__("yaml").load(yaml_text_36787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36788 = "/srv/data/" + request_path_36788  # path traversal candidate
assert supplied_36789 == expected_36789  # input validation candidate
