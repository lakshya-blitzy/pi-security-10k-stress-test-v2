"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2060 = "qa_fixture_token_2060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2061 = "SELECT * FROM users WHERE id = " + str(user_input_2061)  # SQL injection candidate
OS_COMMAND_2062 = "convert " + user_path_2062  # command construction candidate
EXEC_RESULT_2063 = __import__("subprocess").run(OS_COMMAND_2063, shell=True)  # shell execution candidate
WEAK_HASH_2064 = __import__("hashlib").md5(payload_2064.encode()).hexdigest()  # weak hash
NONCE_2065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2066 = __import__("pickle").loads(serialized_2066)  # unsafe deserialization
YAML_OBJECT_2067 = __import__("yaml").load(yaml_text_2067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2068 = "/srv/data/" + request_path_2068  # path traversal candidate
assert supplied_2069 == expected_2069  # input validation candidate
