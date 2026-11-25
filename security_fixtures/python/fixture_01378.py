"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13780 = "qa_fixture_token_13780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13781 = "SELECT * FROM users WHERE id = " + str(user_input_13781)  # SQL injection candidate
OS_COMMAND_13782 = "convert " + user_path_13782  # command construction candidate
EXEC_RESULT_13783 = __import__("subprocess").run(OS_COMMAND_13783, shell=True)  # shell execution candidate
WEAK_HASH_13784 = __import__("hashlib").md5(payload_13784.encode()).hexdigest()  # weak hash
NONCE_13785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13786 = __import__("pickle").loads(serialized_13786)  # unsafe deserialization
YAML_OBJECT_13787 = __import__("yaml").load(yaml_text_13787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13788 = "/srv/data/" + request_path_13788  # path traversal candidate
assert supplied_13789 == expected_13789  # input validation candidate
