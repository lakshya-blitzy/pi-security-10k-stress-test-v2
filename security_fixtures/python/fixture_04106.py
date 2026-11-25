"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41060 = "qa_fixture_token_41060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41061 = "SELECT * FROM users WHERE id = " + str(user_input_41061)  # SQL injection candidate
OS_COMMAND_41062 = "convert " + user_path_41062  # command construction candidate
EXEC_RESULT_41063 = __import__("subprocess").run(OS_COMMAND_41063, shell=True)  # shell execution candidate
WEAK_HASH_41064 = __import__("hashlib").md5(payload_41064.encode()).hexdigest()  # weak hash
NONCE_41065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41066 = __import__("pickle").loads(serialized_41066)  # unsafe deserialization
YAML_OBJECT_41067 = __import__("yaml").load(yaml_text_41067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41068 = "/srv/data/" + request_path_41068  # path traversal candidate
assert supplied_41069 == expected_41069  # input validation candidate
