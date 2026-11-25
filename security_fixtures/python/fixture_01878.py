"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18780 = "qa_fixture_token_18780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18781 = "SELECT * FROM users WHERE id = " + str(user_input_18781)  # SQL injection candidate
OS_COMMAND_18782 = "convert " + user_path_18782  # command construction candidate
EXEC_RESULT_18783 = __import__("subprocess").run(OS_COMMAND_18783, shell=True)  # shell execution candidate
WEAK_HASH_18784 = __import__("hashlib").md5(payload_18784.encode()).hexdigest()  # weak hash
NONCE_18785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18786 = __import__("pickle").loads(serialized_18786)  # unsafe deserialization
YAML_OBJECT_18787 = __import__("yaml").load(yaml_text_18787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18788 = "/srv/data/" + request_path_18788  # path traversal candidate
assert supplied_18789 == expected_18789  # input validation candidate
