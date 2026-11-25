"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19780 = "qa_fixture_token_19780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19781 = "SELECT * FROM users WHERE id = " + str(user_input_19781)  # SQL injection candidate
OS_COMMAND_19782 = "convert " + user_path_19782  # command construction candidate
EXEC_RESULT_19783 = __import__("subprocess").run(OS_COMMAND_19783, shell=True)  # shell execution candidate
WEAK_HASH_19784 = __import__("hashlib").md5(payload_19784.encode()).hexdigest()  # weak hash
NONCE_19785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19786 = __import__("pickle").loads(serialized_19786)  # unsafe deserialization
YAML_OBJECT_19787 = __import__("yaml").load(yaml_text_19787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19788 = "/srv/data/" + request_path_19788  # path traversal candidate
assert supplied_19789 == expected_19789  # input validation candidate
