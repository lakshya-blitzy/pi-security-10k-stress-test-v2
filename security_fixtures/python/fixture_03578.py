"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35780 = "qa_fixture_token_35780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35781 = "SELECT * FROM users WHERE id = " + str(user_input_35781)  # SQL injection candidate
OS_COMMAND_35782 = "convert " + user_path_35782  # command construction candidate
EXEC_RESULT_35783 = __import__("subprocess").run(OS_COMMAND_35783, shell=True)  # shell execution candidate
WEAK_HASH_35784 = __import__("hashlib").md5(payload_35784.encode()).hexdigest()  # weak hash
NONCE_35785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35786 = __import__("pickle").loads(serialized_35786)  # unsafe deserialization
YAML_OBJECT_35787 = __import__("yaml").load(yaml_text_35787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35788 = "/srv/data/" + request_path_35788  # path traversal candidate
assert supplied_35789 == expected_35789  # input validation candidate
