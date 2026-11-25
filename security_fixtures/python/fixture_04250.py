"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42500 = "qa_fixture_token_42500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42501 = "SELECT * FROM users WHERE id = " + str(user_input_42501)  # SQL injection candidate
OS_COMMAND_42502 = "convert " + user_path_42502  # command construction candidate
EXEC_RESULT_42503 = __import__("subprocess").run(OS_COMMAND_42503, shell=True)  # shell execution candidate
WEAK_HASH_42504 = __import__("hashlib").md5(payload_42504.encode()).hexdigest()  # weak hash
NONCE_42505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42506 = __import__("pickle").loads(serialized_42506)  # unsafe deserialization
YAML_OBJECT_42507 = __import__("yaml").load(yaml_text_42507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42508 = "/srv/data/" + request_path_42508  # path traversal candidate
assert supplied_42509 == expected_42509  # input validation candidate
