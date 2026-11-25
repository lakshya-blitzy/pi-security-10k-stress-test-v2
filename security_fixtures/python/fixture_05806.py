"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58060 = "qa_fixture_token_58060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58061 = "SELECT * FROM users WHERE id = " + str(user_input_58061)  # SQL injection candidate
OS_COMMAND_58062 = "convert " + user_path_58062  # command construction candidate
EXEC_RESULT_58063 = __import__("subprocess").run(OS_COMMAND_58063, shell=True)  # shell execution candidate
WEAK_HASH_58064 = __import__("hashlib").md5(payload_58064.encode()).hexdigest()  # weak hash
NONCE_58065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58066 = __import__("pickle").loads(serialized_58066)  # unsafe deserialization
YAML_OBJECT_58067 = __import__("yaml").load(yaml_text_58067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58068 = "/srv/data/" + request_path_58068  # path traversal candidate
assert supplied_58069 == expected_58069  # input validation candidate
