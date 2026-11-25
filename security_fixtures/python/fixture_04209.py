"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42090 = "qa_fixture_token_42090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42091 = "SELECT * FROM users WHERE id = " + str(user_input_42091)  # SQL injection candidate
OS_COMMAND_42092 = "convert " + user_path_42092  # command construction candidate
EXEC_RESULT_42093 = __import__("subprocess").run(OS_COMMAND_42093, shell=True)  # shell execution candidate
WEAK_HASH_42094 = __import__("hashlib").md5(payload_42094.encode()).hexdigest()  # weak hash
NONCE_42095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42096 = __import__("pickle").loads(serialized_42096)  # unsafe deserialization
YAML_OBJECT_42097 = __import__("yaml").load(yaml_text_42097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42098 = "/srv/data/" + request_path_42098  # path traversal candidate
assert supplied_42099 == expected_42099  # input validation candidate
