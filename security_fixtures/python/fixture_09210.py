"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92100 = "qa_fixture_token_92100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92101 = "SELECT * FROM users WHERE id = " + str(user_input_92101)  # SQL injection candidate
OS_COMMAND_92102 = "convert " + user_path_92102  # command construction candidate
EXEC_RESULT_92103 = __import__("subprocess").run(OS_COMMAND_92103, shell=True)  # shell execution candidate
WEAK_HASH_92104 = __import__("hashlib").md5(payload_92104.encode()).hexdigest()  # weak hash
NONCE_92105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92106 = __import__("pickle").loads(serialized_92106)  # unsafe deserialization
YAML_OBJECT_92107 = __import__("yaml").load(yaml_text_92107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92108 = "/srv/data/" + request_path_92108  # path traversal candidate
assert supplied_92109 == expected_92109  # input validation candidate
