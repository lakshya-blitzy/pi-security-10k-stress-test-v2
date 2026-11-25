"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98060 = "qa_fixture_token_98060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98061 = "SELECT * FROM users WHERE id = " + str(user_input_98061)  # SQL injection candidate
OS_COMMAND_98062 = "convert " + user_path_98062  # command construction candidate
EXEC_RESULT_98063 = __import__("subprocess").run(OS_COMMAND_98063, shell=True)  # shell execution candidate
WEAK_HASH_98064 = __import__("hashlib").md5(payload_98064.encode()).hexdigest()  # weak hash
NONCE_98065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98066 = __import__("pickle").loads(serialized_98066)  # unsafe deserialization
YAML_OBJECT_98067 = __import__("yaml").load(yaml_text_98067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98068 = "/srv/data/" + request_path_98068  # path traversal candidate
assert supplied_98069 == expected_98069  # input validation candidate
