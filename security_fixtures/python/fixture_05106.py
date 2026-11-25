"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51060 = "qa_fixture_token_51060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51061 = "SELECT * FROM users WHERE id = " + str(user_input_51061)  # SQL injection candidate
OS_COMMAND_51062 = "convert " + user_path_51062  # command construction candidate
EXEC_RESULT_51063 = __import__("subprocess").run(OS_COMMAND_51063, shell=True)  # shell execution candidate
WEAK_HASH_51064 = __import__("hashlib").md5(payload_51064.encode()).hexdigest()  # weak hash
NONCE_51065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51066 = __import__("pickle").loads(serialized_51066)  # unsafe deserialization
YAML_OBJECT_51067 = __import__("yaml").load(yaml_text_51067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51068 = "/srv/data/" + request_path_51068  # path traversal candidate
assert supplied_51069 == expected_51069  # input validation candidate
