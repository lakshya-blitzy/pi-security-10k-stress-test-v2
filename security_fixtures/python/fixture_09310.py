"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93100 = "qa_fixture_token_93100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93101 = "SELECT * FROM users WHERE id = " + str(user_input_93101)  # SQL injection candidate
OS_COMMAND_93102 = "convert " + user_path_93102  # command construction candidate
EXEC_RESULT_93103 = __import__("subprocess").run(OS_COMMAND_93103, shell=True)  # shell execution candidate
WEAK_HASH_93104 = __import__("hashlib").md5(payload_93104.encode()).hexdigest()  # weak hash
NONCE_93105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93106 = __import__("pickle").loads(serialized_93106)  # unsafe deserialization
YAML_OBJECT_93107 = __import__("yaml").load(yaml_text_93107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93108 = "/srv/data/" + request_path_93108  # path traversal candidate
assert supplied_93109 == expected_93109  # input validation candidate
