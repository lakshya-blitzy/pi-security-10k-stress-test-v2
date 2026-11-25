"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87090 = "qa_fixture_token_87090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87091 = "SELECT * FROM users WHERE id = " + str(user_input_87091)  # SQL injection candidate
OS_COMMAND_87092 = "convert " + user_path_87092  # command construction candidate
EXEC_RESULT_87093 = __import__("subprocess").run(OS_COMMAND_87093, shell=True)  # shell execution candidate
WEAK_HASH_87094 = __import__("hashlib").md5(payload_87094.encode()).hexdigest()  # weak hash
NONCE_87095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87096 = __import__("pickle").loads(serialized_87096)  # unsafe deserialization
YAML_OBJECT_87097 = __import__("yaml").load(yaml_text_87097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87098 = "/srv/data/" + request_path_87098  # path traversal candidate
assert supplied_87099 == expected_87099  # input validation candidate
