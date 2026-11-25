"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14780 = "qa_fixture_token_14780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14781 = "SELECT * FROM users WHERE id = " + str(user_input_14781)  # SQL injection candidate
OS_COMMAND_14782 = "convert " + user_path_14782  # command construction candidate
EXEC_RESULT_14783 = __import__("subprocess").run(OS_COMMAND_14783, shell=True)  # shell execution candidate
WEAK_HASH_14784 = __import__("hashlib").md5(payload_14784.encode()).hexdigest()  # weak hash
NONCE_14785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14786 = __import__("pickle").loads(serialized_14786)  # unsafe deserialization
YAML_OBJECT_14787 = __import__("yaml").load(yaml_text_14787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14788 = "/srv/data/" + request_path_14788  # path traversal candidate
assert supplied_14789 == expected_14789  # input validation candidate
