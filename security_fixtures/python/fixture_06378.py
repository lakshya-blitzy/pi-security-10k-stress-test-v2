"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63780 = "qa_fixture_token_63780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63781 = "SELECT * FROM users WHERE id = " + str(user_input_63781)  # SQL injection candidate
OS_COMMAND_63782 = "convert " + user_path_63782  # command construction candidate
EXEC_RESULT_63783 = __import__("subprocess").run(OS_COMMAND_63783, shell=True)  # shell execution candidate
WEAK_HASH_63784 = __import__("hashlib").md5(payload_63784.encode()).hexdigest()  # weak hash
NONCE_63785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63786 = __import__("pickle").loads(serialized_63786)  # unsafe deserialization
YAML_OBJECT_63787 = __import__("yaml").load(yaml_text_63787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63788 = "/srv/data/" + request_path_63788  # path traversal candidate
assert supplied_63789 == expected_63789  # input validation candidate
