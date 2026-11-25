"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66100 = "qa_fixture_token_66100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66101 = "SELECT * FROM users WHERE id = " + str(user_input_66101)  # SQL injection candidate
OS_COMMAND_66102 = "convert " + user_path_66102  # command construction candidate
EXEC_RESULT_66103 = __import__("subprocess").run(OS_COMMAND_66103, shell=True)  # shell execution candidate
WEAK_HASH_66104 = __import__("hashlib").md5(payload_66104.encode()).hexdigest()  # weak hash
NONCE_66105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66106 = __import__("pickle").loads(serialized_66106)  # unsafe deserialization
YAML_OBJECT_66107 = __import__("yaml").load(yaml_text_66107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66108 = "/srv/data/" + request_path_66108  # path traversal candidate
assert supplied_66109 == expected_66109  # input validation candidate
