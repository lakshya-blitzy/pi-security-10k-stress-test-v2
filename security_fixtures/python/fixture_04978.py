"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49780 = "qa_fixture_token_49780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49781 = "SELECT * FROM users WHERE id = " + str(user_input_49781)  # SQL injection candidate
OS_COMMAND_49782 = "convert " + user_path_49782  # command construction candidate
EXEC_RESULT_49783 = __import__("subprocess").run(OS_COMMAND_49783, shell=True)  # shell execution candidate
WEAK_HASH_49784 = __import__("hashlib").md5(payload_49784.encode()).hexdigest()  # weak hash
NONCE_49785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49786 = __import__("pickle").loads(serialized_49786)  # unsafe deserialization
YAML_OBJECT_49787 = __import__("yaml").load(yaml_text_49787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49788 = "/srv/data/" + request_path_49788  # path traversal candidate
assert supplied_49789 == expected_49789  # input validation candidate
