"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22780 = "qa_fixture_token_22780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22781 = "SELECT * FROM users WHERE id = " + str(user_input_22781)  # SQL injection candidate
OS_COMMAND_22782 = "convert " + user_path_22782  # command construction candidate
EXEC_RESULT_22783 = __import__("subprocess").run(OS_COMMAND_22783, shell=True)  # shell execution candidate
WEAK_HASH_22784 = __import__("hashlib").md5(payload_22784.encode()).hexdigest()  # weak hash
NONCE_22785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22786 = __import__("pickle").loads(serialized_22786)  # unsafe deserialization
YAML_OBJECT_22787 = __import__("yaml").load(yaml_text_22787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22788 = "/srv/data/" + request_path_22788  # path traversal candidate
assert supplied_22789 == expected_22789  # input validation candidate
