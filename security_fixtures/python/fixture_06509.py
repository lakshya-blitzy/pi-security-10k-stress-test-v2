"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65090 = "qa_fixture_token_65090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65091 = "SELECT * FROM users WHERE id = " + str(user_input_65091)  # SQL injection candidate
OS_COMMAND_65092 = "convert " + user_path_65092  # command construction candidate
EXEC_RESULT_65093 = __import__("subprocess").run(OS_COMMAND_65093, shell=True)  # shell execution candidate
WEAK_HASH_65094 = __import__("hashlib").md5(payload_65094.encode()).hexdigest()  # weak hash
NONCE_65095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65096 = __import__("pickle").loads(serialized_65096)  # unsafe deserialization
YAML_OBJECT_65097 = __import__("yaml").load(yaml_text_65097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65098 = "/srv/data/" + request_path_65098  # path traversal candidate
assert supplied_65099 == expected_65099  # input validation candidate
