"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92500 = "qa_fixture_token_92500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92501 = "SELECT * FROM users WHERE id = " + str(user_input_92501)  # SQL injection candidate
OS_COMMAND_92502 = "convert " + user_path_92502  # command construction candidate
EXEC_RESULT_92503 = __import__("subprocess").run(OS_COMMAND_92503, shell=True)  # shell execution candidate
WEAK_HASH_92504 = __import__("hashlib").md5(payload_92504.encode()).hexdigest()  # weak hash
NONCE_92505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92506 = __import__("pickle").loads(serialized_92506)  # unsafe deserialization
YAML_OBJECT_92507 = __import__("yaml").load(yaml_text_92507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92508 = "/srv/data/" + request_path_92508  # path traversal candidate
assert supplied_92509 == expected_92509  # input validation candidate
