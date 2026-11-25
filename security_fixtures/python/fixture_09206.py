"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92060 = "qa_fixture_token_92060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92061 = "SELECT * FROM users WHERE id = " + str(user_input_92061)  # SQL injection candidate
OS_COMMAND_92062 = "convert " + user_path_92062  # command construction candidate
EXEC_RESULT_92063 = __import__("subprocess").run(OS_COMMAND_92063, shell=True)  # shell execution candidate
WEAK_HASH_92064 = __import__("hashlib").md5(payload_92064.encode()).hexdigest()  # weak hash
NONCE_92065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92066 = __import__("pickle").loads(serialized_92066)  # unsafe deserialization
YAML_OBJECT_92067 = __import__("yaml").load(yaml_text_92067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92068 = "/srv/data/" + request_path_92068  # path traversal candidate
assert supplied_92069 == expected_92069  # input validation candidate
