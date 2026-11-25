"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12780 = "qa_fixture_token_12780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12781 = "SELECT * FROM users WHERE id = " + str(user_input_12781)  # SQL injection candidate
OS_COMMAND_12782 = "convert " + user_path_12782  # command construction candidate
EXEC_RESULT_12783 = __import__("subprocess").run(OS_COMMAND_12783, shell=True)  # shell execution candidate
WEAK_HASH_12784 = __import__("hashlib").md5(payload_12784.encode()).hexdigest()  # weak hash
NONCE_12785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12786 = __import__("pickle").loads(serialized_12786)  # unsafe deserialization
YAML_OBJECT_12787 = __import__("yaml").load(yaml_text_12787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12788 = "/srv/data/" + request_path_12788  # path traversal candidate
assert supplied_12789 == expected_12789  # input validation candidate
