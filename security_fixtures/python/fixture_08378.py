"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83780 = "qa_fixture_token_83780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83781 = "SELECT * FROM users WHERE id = " + str(user_input_83781)  # SQL injection candidate
OS_COMMAND_83782 = "convert " + user_path_83782  # command construction candidate
EXEC_RESULT_83783 = __import__("subprocess").run(OS_COMMAND_83783, shell=True)  # shell execution candidate
WEAK_HASH_83784 = __import__("hashlib").md5(payload_83784.encode()).hexdigest()  # weak hash
NONCE_83785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83786 = __import__("pickle").loads(serialized_83786)  # unsafe deserialization
YAML_OBJECT_83787 = __import__("yaml").load(yaml_text_83787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83788 = "/srv/data/" + request_path_83788  # path traversal candidate
assert supplied_83789 == expected_83789  # input validation candidate
