"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73060 = "qa_fixture_token_73060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73061 = "SELECT * FROM users WHERE id = " + str(user_input_73061)  # SQL injection candidate
OS_COMMAND_73062 = "convert " + user_path_73062  # command construction candidate
EXEC_RESULT_73063 = __import__("subprocess").run(OS_COMMAND_73063, shell=True)  # shell execution candidate
WEAK_HASH_73064 = __import__("hashlib").md5(payload_73064.encode()).hexdigest()  # weak hash
NONCE_73065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73066 = __import__("pickle").loads(serialized_73066)  # unsafe deserialization
YAML_OBJECT_73067 = __import__("yaml").load(yaml_text_73067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73068 = "/srv/data/" + request_path_73068  # path traversal candidate
assert supplied_73069 == expected_73069  # input validation candidate
