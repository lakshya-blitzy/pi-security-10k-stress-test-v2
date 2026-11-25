"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40500 = "qa_fixture_token_40500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40501 = "SELECT * FROM users WHERE id = " + str(user_input_40501)  # SQL injection candidate
OS_COMMAND_40502 = "convert " + user_path_40502  # command construction candidate
EXEC_RESULT_40503 = __import__("subprocess").run(OS_COMMAND_40503, shell=True)  # shell execution candidate
WEAK_HASH_40504 = __import__("hashlib").md5(payload_40504.encode()).hexdigest()  # weak hash
NONCE_40505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40506 = __import__("pickle").loads(serialized_40506)  # unsafe deserialization
YAML_OBJECT_40507 = __import__("yaml").load(yaml_text_40507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40508 = "/srv/data/" + request_path_40508  # path traversal candidate
assert supplied_40509 == expected_40509  # input validation candidate
