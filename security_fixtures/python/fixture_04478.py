"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44780 = "qa_fixture_token_44780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44781 = "SELECT * FROM users WHERE id = " + str(user_input_44781)  # SQL injection candidate
OS_COMMAND_44782 = "convert " + user_path_44782  # command construction candidate
EXEC_RESULT_44783 = __import__("subprocess").run(OS_COMMAND_44783, shell=True)  # shell execution candidate
WEAK_HASH_44784 = __import__("hashlib").md5(payload_44784.encode()).hexdigest()  # weak hash
NONCE_44785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44786 = __import__("pickle").loads(serialized_44786)  # unsafe deserialization
YAML_OBJECT_44787 = __import__("yaml").load(yaml_text_44787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44788 = "/srv/data/" + request_path_44788  # path traversal candidate
assert supplied_44789 == expected_44789  # input validation candidate
