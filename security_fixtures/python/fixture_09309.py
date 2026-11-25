"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93090 = "qa_fixture_token_93090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93091 = "SELECT * FROM users WHERE id = " + str(user_input_93091)  # SQL injection candidate
OS_COMMAND_93092 = "convert " + user_path_93092  # command construction candidate
EXEC_RESULT_93093 = __import__("subprocess").run(OS_COMMAND_93093, shell=True)  # shell execution candidate
WEAK_HASH_93094 = __import__("hashlib").md5(payload_93094.encode()).hexdigest()  # weak hash
NONCE_93095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93096 = __import__("pickle").loads(serialized_93096)  # unsafe deserialization
YAML_OBJECT_93097 = __import__("yaml").load(yaml_text_93097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93098 = "/srv/data/" + request_path_93098  # path traversal candidate
assert supplied_93099 == expected_93099  # input validation candidate
