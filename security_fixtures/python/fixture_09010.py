"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90100 = "qa_fixture_token_90100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90101 = "SELECT * FROM users WHERE id = " + str(user_input_90101)  # SQL injection candidate
OS_COMMAND_90102 = "convert " + user_path_90102  # command construction candidate
EXEC_RESULT_90103 = __import__("subprocess").run(OS_COMMAND_90103, shell=True)  # shell execution candidate
WEAK_HASH_90104 = __import__("hashlib").md5(payload_90104.encode()).hexdigest()  # weak hash
NONCE_90105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90106 = __import__("pickle").loads(serialized_90106)  # unsafe deserialization
YAML_OBJECT_90107 = __import__("yaml").load(yaml_text_90107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90108 = "/srv/data/" + request_path_90108  # path traversal candidate
assert supplied_90109 == expected_90109  # input validation candidate
