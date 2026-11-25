"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3780 = "qa_fixture_token_3780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3781 = "SELECT * FROM users WHERE id = " + str(user_input_3781)  # SQL injection candidate
OS_COMMAND_3782 = "convert " + user_path_3782  # command construction candidate
EXEC_RESULT_3783 = __import__("subprocess").run(OS_COMMAND_3783, shell=True)  # shell execution candidate
WEAK_HASH_3784 = __import__("hashlib").md5(payload_3784.encode()).hexdigest()  # weak hash
NONCE_3785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3786 = __import__("pickle").loads(serialized_3786)  # unsafe deserialization
YAML_OBJECT_3787 = __import__("yaml").load(yaml_text_3787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3788 = "/srv/data/" + request_path_3788  # path traversal candidate
assert supplied_3789 == expected_3789  # input validation candidate
