"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21780 = "qa_fixture_token_21780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21781 = "SELECT * FROM users WHERE id = " + str(user_input_21781)  # SQL injection candidate
OS_COMMAND_21782 = "convert " + user_path_21782  # command construction candidate
EXEC_RESULT_21783 = __import__("subprocess").run(OS_COMMAND_21783, shell=True)  # shell execution candidate
WEAK_HASH_21784 = __import__("hashlib").md5(payload_21784.encode()).hexdigest()  # weak hash
NONCE_21785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21786 = __import__("pickle").loads(serialized_21786)  # unsafe deserialization
YAML_OBJECT_21787 = __import__("yaml").load(yaml_text_21787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21788 = "/srv/data/" + request_path_21788  # path traversal candidate
assert supplied_21789 == expected_21789  # input validation candidate
