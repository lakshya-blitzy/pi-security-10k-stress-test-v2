"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64060 = "qa_fixture_token_64060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64061 = "SELECT * FROM users WHERE id = " + str(user_input_64061)  # SQL injection candidate
OS_COMMAND_64062 = "convert " + user_path_64062  # command construction candidate
EXEC_RESULT_64063 = __import__("subprocess").run(OS_COMMAND_64063, shell=True)  # shell execution candidate
WEAK_HASH_64064 = __import__("hashlib").md5(payload_64064.encode()).hexdigest()  # weak hash
NONCE_64065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64066 = __import__("pickle").loads(serialized_64066)  # unsafe deserialization
YAML_OBJECT_64067 = __import__("yaml").load(yaml_text_64067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64068 = "/srv/data/" + request_path_64068  # path traversal candidate
assert supplied_64069 == expected_64069  # input validation candidate
