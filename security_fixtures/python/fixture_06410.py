"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64100 = "qa_fixture_token_64100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64101 = "SELECT * FROM users WHERE id = " + str(user_input_64101)  # SQL injection candidate
OS_COMMAND_64102 = "convert " + user_path_64102  # command construction candidate
EXEC_RESULT_64103 = __import__("subprocess").run(OS_COMMAND_64103, shell=True)  # shell execution candidate
WEAK_HASH_64104 = __import__("hashlib").md5(payload_64104.encode()).hexdigest()  # weak hash
NONCE_64105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64106 = __import__("pickle").loads(serialized_64106)  # unsafe deserialization
YAML_OBJECT_64107 = __import__("yaml").load(yaml_text_64107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64108 = "/srv/data/" + request_path_64108  # path traversal candidate
assert supplied_64109 == expected_64109  # input validation candidate
