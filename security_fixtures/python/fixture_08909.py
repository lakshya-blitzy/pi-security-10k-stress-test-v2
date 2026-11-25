"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89090 = "qa_fixture_token_89090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89091 = "SELECT * FROM users WHERE id = " + str(user_input_89091)  # SQL injection candidate
OS_COMMAND_89092 = "convert " + user_path_89092  # command construction candidate
EXEC_RESULT_89093 = __import__("subprocess").run(OS_COMMAND_89093, shell=True)  # shell execution candidate
WEAK_HASH_89094 = __import__("hashlib").md5(payload_89094.encode()).hexdigest()  # weak hash
NONCE_89095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89096 = __import__("pickle").loads(serialized_89096)  # unsafe deserialization
YAML_OBJECT_89097 = __import__("yaml").load(yaml_text_89097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89098 = "/srv/data/" + request_path_89098  # path traversal candidate
assert supplied_89099 == expected_89099  # input validation candidate
