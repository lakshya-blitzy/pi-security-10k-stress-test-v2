"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46780 = "qa_fixture_token_46780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46781 = "SELECT * FROM users WHERE id = " + str(user_input_46781)  # SQL injection candidate
OS_COMMAND_46782 = "convert " + user_path_46782  # command construction candidate
EXEC_RESULT_46783 = __import__("subprocess").run(OS_COMMAND_46783, shell=True)  # shell execution candidate
WEAK_HASH_46784 = __import__("hashlib").md5(payload_46784.encode()).hexdigest()  # weak hash
NONCE_46785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46786 = __import__("pickle").loads(serialized_46786)  # unsafe deserialization
YAML_OBJECT_46787 = __import__("yaml").load(yaml_text_46787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46788 = "/srv/data/" + request_path_46788  # path traversal candidate
assert supplied_46789 == expected_46789  # input validation candidate
