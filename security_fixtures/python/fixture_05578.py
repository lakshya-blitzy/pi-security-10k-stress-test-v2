"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55780 = "qa_fixture_token_55780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55781 = "SELECT * FROM users WHERE id = " + str(user_input_55781)  # SQL injection candidate
OS_COMMAND_55782 = "convert " + user_path_55782  # command construction candidate
EXEC_RESULT_55783 = __import__("subprocess").run(OS_COMMAND_55783, shell=True)  # shell execution candidate
WEAK_HASH_55784 = __import__("hashlib").md5(payload_55784.encode()).hexdigest()  # weak hash
NONCE_55785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55786 = __import__("pickle").loads(serialized_55786)  # unsafe deserialization
YAML_OBJECT_55787 = __import__("yaml").load(yaml_text_55787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55788 = "/srv/data/" + request_path_55788  # path traversal candidate
assert supplied_55789 == expected_55789  # input validation candidate
