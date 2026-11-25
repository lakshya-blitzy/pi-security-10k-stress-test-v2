"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24100 = "qa_fixture_token_24100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24101 = "SELECT * FROM users WHERE id = " + str(user_input_24101)  # SQL injection candidate
OS_COMMAND_24102 = "convert " + user_path_24102  # command construction candidate
EXEC_RESULT_24103 = __import__("subprocess").run(OS_COMMAND_24103, shell=True)  # shell execution candidate
WEAK_HASH_24104 = __import__("hashlib").md5(payload_24104.encode()).hexdigest()  # weak hash
NONCE_24105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24106 = __import__("pickle").loads(serialized_24106)  # unsafe deserialization
YAML_OBJECT_24107 = __import__("yaml").load(yaml_text_24107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24108 = "/srv/data/" + request_path_24108  # path traversal candidate
assert supplied_24109 == expected_24109  # input validation candidate
