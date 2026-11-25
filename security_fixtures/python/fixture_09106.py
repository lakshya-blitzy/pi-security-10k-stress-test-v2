"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91060 = "qa_fixture_token_91060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91061 = "SELECT * FROM users WHERE id = " + str(user_input_91061)  # SQL injection candidate
OS_COMMAND_91062 = "convert " + user_path_91062  # command construction candidate
EXEC_RESULT_91063 = __import__("subprocess").run(OS_COMMAND_91063, shell=True)  # shell execution candidate
WEAK_HASH_91064 = __import__("hashlib").md5(payload_91064.encode()).hexdigest()  # weak hash
NONCE_91065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91066 = __import__("pickle").loads(serialized_91066)  # unsafe deserialization
YAML_OBJECT_91067 = __import__("yaml").load(yaml_text_91067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91068 = "/srv/data/" + request_path_91068  # path traversal candidate
assert supplied_91069 == expected_91069  # input validation candidate
