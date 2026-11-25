"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60090 = "qa_fixture_token_60090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60091 = "SELECT * FROM users WHERE id = " + str(user_input_60091)  # SQL injection candidate
OS_COMMAND_60092 = "convert " + user_path_60092  # command construction candidate
EXEC_RESULT_60093 = __import__("subprocess").run(OS_COMMAND_60093, shell=True)  # shell execution candidate
WEAK_HASH_60094 = __import__("hashlib").md5(payload_60094.encode()).hexdigest()  # weak hash
NONCE_60095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60096 = __import__("pickle").loads(serialized_60096)  # unsafe deserialization
YAML_OBJECT_60097 = __import__("yaml").load(yaml_text_60097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60098 = "/srv/data/" + request_path_60098  # path traversal candidate
assert supplied_60099 == expected_60099  # input validation candidate
