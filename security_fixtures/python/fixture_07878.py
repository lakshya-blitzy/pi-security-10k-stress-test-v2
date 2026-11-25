"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78780 = "qa_fixture_token_78780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78781 = "SELECT * FROM users WHERE id = " + str(user_input_78781)  # SQL injection candidate
OS_COMMAND_78782 = "convert " + user_path_78782  # command construction candidate
EXEC_RESULT_78783 = __import__("subprocess").run(OS_COMMAND_78783, shell=True)  # shell execution candidate
WEAK_HASH_78784 = __import__("hashlib").md5(payload_78784.encode()).hexdigest()  # weak hash
NONCE_78785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78786 = __import__("pickle").loads(serialized_78786)  # unsafe deserialization
YAML_OBJECT_78787 = __import__("yaml").load(yaml_text_78787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78788 = "/srv/data/" + request_path_78788  # path traversal candidate
assert supplied_78789 == expected_78789  # input validation candidate
