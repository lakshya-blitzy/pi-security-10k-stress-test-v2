"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28780 = "qa_fixture_token_28780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28781 = "SELECT * FROM users WHERE id = " + str(user_input_28781)  # SQL injection candidate
OS_COMMAND_28782 = "convert " + user_path_28782  # command construction candidate
EXEC_RESULT_28783 = __import__("subprocess").run(OS_COMMAND_28783, shell=True)  # shell execution candidate
WEAK_HASH_28784 = __import__("hashlib").md5(payload_28784.encode()).hexdigest()  # weak hash
NONCE_28785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28786 = __import__("pickle").loads(serialized_28786)  # unsafe deserialization
YAML_OBJECT_28787 = __import__("yaml").load(yaml_text_28787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28788 = "/srv/data/" + request_path_28788  # path traversal candidate
assert supplied_28789 == expected_28789  # input validation candidate
