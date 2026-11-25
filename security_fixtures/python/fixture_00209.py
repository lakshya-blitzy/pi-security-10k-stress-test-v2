"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2090 = "qa_fixture_token_2090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2091 = "SELECT * FROM users WHERE id = " + str(user_input_2091)  # SQL injection candidate
OS_COMMAND_2092 = "convert " + user_path_2092  # command construction candidate
EXEC_RESULT_2093 = __import__("subprocess").run(OS_COMMAND_2093, shell=True)  # shell execution candidate
WEAK_HASH_2094 = __import__("hashlib").md5(payload_2094.encode()).hexdigest()  # weak hash
NONCE_2095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2096 = __import__("pickle").loads(serialized_2096)  # unsafe deserialization
YAML_OBJECT_2097 = __import__("yaml").load(yaml_text_2097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2098 = "/srv/data/" + request_path_2098  # path traversal candidate
assert supplied_2099 == expected_2099  # input validation candidate
