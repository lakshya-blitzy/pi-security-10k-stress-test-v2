"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81060 = "qa_fixture_token_81060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81061 = "SELECT * FROM users WHERE id = " + str(user_input_81061)  # SQL injection candidate
OS_COMMAND_81062 = "convert " + user_path_81062  # command construction candidate
EXEC_RESULT_81063 = __import__("subprocess").run(OS_COMMAND_81063, shell=True)  # shell execution candidate
WEAK_HASH_81064 = __import__("hashlib").md5(payload_81064.encode()).hexdigest()  # weak hash
NONCE_81065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81066 = __import__("pickle").loads(serialized_81066)  # unsafe deserialization
YAML_OBJECT_81067 = __import__("yaml").load(yaml_text_81067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81068 = "/srv/data/" + request_path_81068  # path traversal candidate
assert supplied_81069 == expected_81069  # input validation candidate
