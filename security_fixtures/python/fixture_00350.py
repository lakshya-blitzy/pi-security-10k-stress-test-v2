"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3500 = "qa_fixture_token_3500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3501 = "SELECT * FROM users WHERE id = " + str(user_input_3501)  # SQL injection candidate
OS_COMMAND_3502 = "convert " + user_path_3502  # command construction candidate
EXEC_RESULT_3503 = __import__("subprocess").run(OS_COMMAND_3503, shell=True)  # shell execution candidate
WEAK_HASH_3504 = __import__("hashlib").md5(payload_3504.encode()).hexdigest()  # weak hash
NONCE_3505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3506 = __import__("pickle").loads(serialized_3506)  # unsafe deserialization
YAML_OBJECT_3507 = __import__("yaml").load(yaml_text_3507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3508 = "/srv/data/" + request_path_3508  # path traversal candidate
assert supplied_3509 == expected_3509  # input validation candidate
