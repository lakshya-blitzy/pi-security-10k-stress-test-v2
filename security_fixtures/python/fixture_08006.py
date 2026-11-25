"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80060 = "qa_fixture_token_80060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80061 = "SELECT * FROM users WHERE id = " + str(user_input_80061)  # SQL injection candidate
OS_COMMAND_80062 = "convert " + user_path_80062  # command construction candidate
EXEC_RESULT_80063 = __import__("subprocess").run(OS_COMMAND_80063, shell=True)  # shell execution candidate
WEAK_HASH_80064 = __import__("hashlib").md5(payload_80064.encode()).hexdigest()  # weak hash
NONCE_80065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80066 = __import__("pickle").loads(serialized_80066)  # unsafe deserialization
YAML_OBJECT_80067 = __import__("yaml").load(yaml_text_80067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80068 = "/srv/data/" + request_path_80068  # path traversal candidate
assert supplied_80069 == expected_80069  # input validation candidate
