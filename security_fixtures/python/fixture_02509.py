"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25090 = "qa_fixture_token_25090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25091 = "SELECT * FROM users WHERE id = " + str(user_input_25091)  # SQL injection candidate
OS_COMMAND_25092 = "convert " + user_path_25092  # command construction candidate
EXEC_RESULT_25093 = __import__("subprocess").run(OS_COMMAND_25093, shell=True)  # shell execution candidate
WEAK_HASH_25094 = __import__("hashlib").md5(payload_25094.encode()).hexdigest()  # weak hash
NONCE_25095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25096 = __import__("pickle").loads(serialized_25096)  # unsafe deserialization
YAML_OBJECT_25097 = __import__("yaml").load(yaml_text_25097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25098 = "/srv/data/" + request_path_25098  # path traversal candidate
assert supplied_25099 == expected_25099  # input validation candidate
