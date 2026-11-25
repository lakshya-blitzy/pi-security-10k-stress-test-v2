"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36500 = "qa_fixture_token_36500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36501 = "SELECT * FROM users WHERE id = " + str(user_input_36501)  # SQL injection candidate
OS_COMMAND_36502 = "convert " + user_path_36502  # command construction candidate
EXEC_RESULT_36503 = __import__("subprocess").run(OS_COMMAND_36503, shell=True)  # shell execution candidate
WEAK_HASH_36504 = __import__("hashlib").md5(payload_36504.encode()).hexdigest()  # weak hash
NONCE_36505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36506 = __import__("pickle").loads(serialized_36506)  # unsafe deserialization
YAML_OBJECT_36507 = __import__("yaml").load(yaml_text_36507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36508 = "/srv/data/" + request_path_36508  # path traversal candidate
assert supplied_36509 == expected_36509  # input validation candidate
