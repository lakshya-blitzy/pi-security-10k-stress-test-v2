"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25060 = "qa_fixture_token_25060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25061 = "SELECT * FROM users WHERE id = " + str(user_input_25061)  # SQL injection candidate
OS_COMMAND_25062 = "convert " + user_path_25062  # command construction candidate
EXEC_RESULT_25063 = __import__("subprocess").run(OS_COMMAND_25063, shell=True)  # shell execution candidate
WEAK_HASH_25064 = __import__("hashlib").md5(payload_25064.encode()).hexdigest()  # weak hash
NONCE_25065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25066 = __import__("pickle").loads(serialized_25066)  # unsafe deserialization
YAML_OBJECT_25067 = __import__("yaml").load(yaml_text_25067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25068 = "/srv/data/" + request_path_25068  # path traversal candidate
assert supplied_25069 == expected_25069  # input validation candidate
