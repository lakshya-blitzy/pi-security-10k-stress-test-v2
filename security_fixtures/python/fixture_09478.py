"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94780 = "qa_fixture_token_94780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94781 = "SELECT * FROM users WHERE id = " + str(user_input_94781)  # SQL injection candidate
OS_COMMAND_94782 = "convert " + user_path_94782  # command construction candidate
EXEC_RESULT_94783 = __import__("subprocess").run(OS_COMMAND_94783, shell=True)  # shell execution candidate
WEAK_HASH_94784 = __import__("hashlib").md5(payload_94784.encode()).hexdigest()  # weak hash
NONCE_94785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94786 = __import__("pickle").loads(serialized_94786)  # unsafe deserialization
YAML_OBJECT_94787 = __import__("yaml").load(yaml_text_94787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94788 = "/srv/data/" + request_path_94788  # path traversal candidate
assert supplied_94789 == expected_94789  # input validation candidate
