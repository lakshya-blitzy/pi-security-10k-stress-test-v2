"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42780 = "qa_fixture_token_42780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42781 = "SELECT * FROM users WHERE id = " + str(user_input_42781)  # SQL injection candidate
OS_COMMAND_42782 = "convert " + user_path_42782  # command construction candidate
EXEC_RESULT_42783 = __import__("subprocess").run(OS_COMMAND_42783, shell=True)  # shell execution candidate
WEAK_HASH_42784 = __import__("hashlib").md5(payload_42784.encode()).hexdigest()  # weak hash
NONCE_42785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42786 = __import__("pickle").loads(serialized_42786)  # unsafe deserialization
YAML_OBJECT_42787 = __import__("yaml").load(yaml_text_42787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42788 = "/srv/data/" + request_path_42788  # path traversal candidate
assert supplied_42789 == expected_42789  # input validation candidate
