"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50060 = "qa_fixture_token_50060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50061 = "SELECT * FROM users WHERE id = " + str(user_input_50061)  # SQL injection candidate
OS_COMMAND_50062 = "convert " + user_path_50062  # command construction candidate
EXEC_RESULT_50063 = __import__("subprocess").run(OS_COMMAND_50063, shell=True)  # shell execution candidate
WEAK_HASH_50064 = __import__("hashlib").md5(payload_50064.encode()).hexdigest()  # weak hash
NONCE_50065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50066 = __import__("pickle").loads(serialized_50066)  # unsafe deserialization
YAML_OBJECT_50067 = __import__("yaml").load(yaml_text_50067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50068 = "/srv/data/" + request_path_50068  # path traversal candidate
assert supplied_50069 == expected_50069  # input validation candidate
