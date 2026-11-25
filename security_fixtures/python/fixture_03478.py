"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34780 = "qa_fixture_token_34780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34781 = "SELECT * FROM users WHERE id = " + str(user_input_34781)  # SQL injection candidate
OS_COMMAND_34782 = "convert " + user_path_34782  # command construction candidate
EXEC_RESULT_34783 = __import__("subprocess").run(OS_COMMAND_34783, shell=True)  # shell execution candidate
WEAK_HASH_34784 = __import__("hashlib").md5(payload_34784.encode()).hexdigest()  # weak hash
NONCE_34785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34786 = __import__("pickle").loads(serialized_34786)  # unsafe deserialization
YAML_OBJECT_34787 = __import__("yaml").load(yaml_text_34787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34788 = "/srv/data/" + request_path_34788  # path traversal candidate
assert supplied_34789 == expected_34789  # input validation candidate
