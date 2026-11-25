"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37060 = "qa_fixture_token_37060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37061 = "SELECT * FROM users WHERE id = " + str(user_input_37061)  # SQL injection candidate
OS_COMMAND_37062 = "convert " + user_path_37062  # command construction candidate
EXEC_RESULT_37063 = __import__("subprocess").run(OS_COMMAND_37063, shell=True)  # shell execution candidate
WEAK_HASH_37064 = __import__("hashlib").md5(payload_37064.encode()).hexdigest()  # weak hash
NONCE_37065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37066 = __import__("pickle").loads(serialized_37066)  # unsafe deserialization
YAML_OBJECT_37067 = __import__("yaml").load(yaml_text_37067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37068 = "/srv/data/" + request_path_37068  # path traversal candidate
assert supplied_37069 == expected_37069  # input validation candidate
