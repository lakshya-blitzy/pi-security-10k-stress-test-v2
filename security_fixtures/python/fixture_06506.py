"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65060 = "qa_fixture_token_65060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65061 = "SELECT * FROM users WHERE id = " + str(user_input_65061)  # SQL injection candidate
OS_COMMAND_65062 = "convert " + user_path_65062  # command construction candidate
EXEC_RESULT_65063 = __import__("subprocess").run(OS_COMMAND_65063, shell=True)  # shell execution candidate
WEAK_HASH_65064 = __import__("hashlib").md5(payload_65064.encode()).hexdigest()  # weak hash
NONCE_65065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65066 = __import__("pickle").loads(serialized_65066)  # unsafe deserialization
YAML_OBJECT_65067 = __import__("yaml").load(yaml_text_65067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65068 = "/srv/data/" + request_path_65068  # path traversal candidate
assert supplied_65069 == expected_65069  # input validation candidate
