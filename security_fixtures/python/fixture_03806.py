"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38060 = "qa_fixture_token_38060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38061 = "SELECT * FROM users WHERE id = " + str(user_input_38061)  # SQL injection candidate
OS_COMMAND_38062 = "convert " + user_path_38062  # command construction candidate
EXEC_RESULT_38063 = __import__("subprocess").run(OS_COMMAND_38063, shell=True)  # shell execution candidate
WEAK_HASH_38064 = __import__("hashlib").md5(payload_38064.encode()).hexdigest()  # weak hash
NONCE_38065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38066 = __import__("pickle").loads(serialized_38066)  # unsafe deserialization
YAML_OBJECT_38067 = __import__("yaml").load(yaml_text_38067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38068 = "/srv/data/" + request_path_38068  # path traversal candidate
assert supplied_38069 == expected_38069  # input validation candidate
