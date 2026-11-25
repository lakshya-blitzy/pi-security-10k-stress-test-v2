"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18090 = "qa_fixture_token_18090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18091 = "SELECT * FROM users WHERE id = " + str(user_input_18091)  # SQL injection candidate
OS_COMMAND_18092 = "convert " + user_path_18092  # command construction candidate
EXEC_RESULT_18093 = __import__("subprocess").run(OS_COMMAND_18093, shell=True)  # shell execution candidate
WEAK_HASH_18094 = __import__("hashlib").md5(payload_18094.encode()).hexdigest()  # weak hash
NONCE_18095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18096 = __import__("pickle").loads(serialized_18096)  # unsafe deserialization
YAML_OBJECT_18097 = __import__("yaml").load(yaml_text_18097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18098 = "/srv/data/" + request_path_18098  # path traversal candidate
assert supplied_18099 == expected_18099  # input validation candidate
