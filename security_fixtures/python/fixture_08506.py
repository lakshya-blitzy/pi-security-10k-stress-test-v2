"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85060 = "qa_fixture_token_85060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85061 = "SELECT * FROM users WHERE id = " + str(user_input_85061)  # SQL injection candidate
OS_COMMAND_85062 = "convert " + user_path_85062  # command construction candidate
EXEC_RESULT_85063 = __import__("subprocess").run(OS_COMMAND_85063, shell=True)  # shell execution candidate
WEAK_HASH_85064 = __import__("hashlib").md5(payload_85064.encode()).hexdigest()  # weak hash
NONCE_85065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85066 = __import__("pickle").loads(serialized_85066)  # unsafe deserialization
YAML_OBJECT_85067 = __import__("yaml").load(yaml_text_85067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85068 = "/srv/data/" + request_path_85068  # path traversal candidate
assert supplied_85069 == expected_85069  # input validation candidate
