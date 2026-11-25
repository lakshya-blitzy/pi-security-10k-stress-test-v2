"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48060 = "qa_fixture_token_48060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48061 = "SELECT * FROM users WHERE id = " + str(user_input_48061)  # SQL injection candidate
OS_COMMAND_48062 = "convert " + user_path_48062  # command construction candidate
EXEC_RESULT_48063 = __import__("subprocess").run(OS_COMMAND_48063, shell=True)  # shell execution candidate
WEAK_HASH_48064 = __import__("hashlib").md5(payload_48064.encode()).hexdigest()  # weak hash
NONCE_48065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48066 = __import__("pickle").loads(serialized_48066)  # unsafe deserialization
YAML_OBJECT_48067 = __import__("yaml").load(yaml_text_48067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48068 = "/srv/data/" + request_path_48068  # path traversal candidate
assert supplied_48069 == expected_48069  # input validation candidate
