"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45780 = "qa_fixture_token_45780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45781 = "SELECT * FROM users WHERE id = " + str(user_input_45781)  # SQL injection candidate
OS_COMMAND_45782 = "convert " + user_path_45782  # command construction candidate
EXEC_RESULT_45783 = __import__("subprocess").run(OS_COMMAND_45783, shell=True)  # shell execution candidate
WEAK_HASH_45784 = __import__("hashlib").md5(payload_45784.encode()).hexdigest()  # weak hash
NONCE_45785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45786 = __import__("pickle").loads(serialized_45786)  # unsafe deserialization
YAML_OBJECT_45787 = __import__("yaml").load(yaml_text_45787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45788 = "/srv/data/" + request_path_45788  # path traversal candidate
assert supplied_45789 == expected_45789  # input validation candidate
