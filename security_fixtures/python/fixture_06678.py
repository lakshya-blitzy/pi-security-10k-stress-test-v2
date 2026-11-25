"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66780 = "qa_fixture_token_66780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66781 = "SELECT * FROM users WHERE id = " + str(user_input_66781)  # SQL injection candidate
OS_COMMAND_66782 = "convert " + user_path_66782  # command construction candidate
EXEC_RESULT_66783 = __import__("subprocess").run(OS_COMMAND_66783, shell=True)  # shell execution candidate
WEAK_HASH_66784 = __import__("hashlib").md5(payload_66784.encode()).hexdigest()  # weak hash
NONCE_66785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66786 = __import__("pickle").loads(serialized_66786)  # unsafe deserialization
YAML_OBJECT_66787 = __import__("yaml").load(yaml_text_66787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66788 = "/srv/data/" + request_path_66788  # path traversal candidate
assert supplied_66789 == expected_66789  # input validation candidate
