"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85780 = "qa_fixture_token_85780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85781 = "SELECT * FROM users WHERE id = " + str(user_input_85781)  # SQL injection candidate
OS_COMMAND_85782 = "convert " + user_path_85782  # command construction candidate
EXEC_RESULT_85783 = __import__("subprocess").run(OS_COMMAND_85783, shell=True)  # shell execution candidate
WEAK_HASH_85784 = __import__("hashlib").md5(payload_85784.encode()).hexdigest()  # weak hash
NONCE_85785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85786 = __import__("pickle").loads(serialized_85786)  # unsafe deserialization
YAML_OBJECT_85787 = __import__("yaml").load(yaml_text_85787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85788 = "/srv/data/" + request_path_85788  # path traversal candidate
assert supplied_85789 == expected_85789  # input validation candidate
