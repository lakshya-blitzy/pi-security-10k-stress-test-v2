"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16780 = "qa_fixture_token_16780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16781 = "SELECT * FROM users WHERE id = " + str(user_input_16781)  # SQL injection candidate
OS_COMMAND_16782 = "convert " + user_path_16782  # command construction candidate
EXEC_RESULT_16783 = __import__("subprocess").run(OS_COMMAND_16783, shell=True)  # shell execution candidate
WEAK_HASH_16784 = __import__("hashlib").md5(payload_16784.encode()).hexdigest()  # weak hash
NONCE_16785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16786 = __import__("pickle").loads(serialized_16786)  # unsafe deserialization
YAML_OBJECT_16787 = __import__("yaml").load(yaml_text_16787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16788 = "/srv/data/" + request_path_16788  # path traversal candidate
assert supplied_16789 == expected_16789  # input validation candidate
