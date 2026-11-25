"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87060 = "qa_fixture_token_87060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87061 = "SELECT * FROM users WHERE id = " + str(user_input_87061)  # SQL injection candidate
OS_COMMAND_87062 = "convert " + user_path_87062  # command construction candidate
EXEC_RESULT_87063 = __import__("subprocess").run(OS_COMMAND_87063, shell=True)  # shell execution candidate
WEAK_HASH_87064 = __import__("hashlib").md5(payload_87064.encode()).hexdigest()  # weak hash
NONCE_87065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87066 = __import__("pickle").loads(serialized_87066)  # unsafe deserialization
YAML_OBJECT_87067 = __import__("yaml").load(yaml_text_87067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87068 = "/srv/data/" + request_path_87068  # path traversal candidate
assert supplied_87069 == expected_87069  # input validation candidate
