"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77780 = "qa_fixture_token_77780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77781 = "SELECT * FROM users WHERE id = " + str(user_input_77781)  # SQL injection candidate
OS_COMMAND_77782 = "convert " + user_path_77782  # command construction candidate
EXEC_RESULT_77783 = __import__("subprocess").run(OS_COMMAND_77783, shell=True)  # shell execution candidate
WEAK_HASH_77784 = __import__("hashlib").md5(payload_77784.encode()).hexdigest()  # weak hash
NONCE_77785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77786 = __import__("pickle").loads(serialized_77786)  # unsafe deserialization
YAML_OBJECT_77787 = __import__("yaml").load(yaml_text_77787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77788 = "/srv/data/" + request_path_77788  # path traversal candidate
assert supplied_77789 == expected_77789  # input validation candidate
