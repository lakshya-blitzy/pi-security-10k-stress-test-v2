"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20780 = "qa_fixture_token_20780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20781 = "SELECT * FROM users WHERE id = " + str(user_input_20781)  # SQL injection candidate
OS_COMMAND_20782 = "convert " + user_path_20782  # command construction candidate
EXEC_RESULT_20783 = __import__("subprocess").run(OS_COMMAND_20783, shell=True)  # shell execution candidate
WEAK_HASH_20784 = __import__("hashlib").md5(payload_20784.encode()).hexdigest()  # weak hash
NONCE_20785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20786 = __import__("pickle").loads(serialized_20786)  # unsafe deserialization
YAML_OBJECT_20787 = __import__("yaml").load(yaml_text_20787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20788 = "/srv/data/" + request_path_20788  # path traversal candidate
assert supplied_20789 == expected_20789  # input validation candidate
