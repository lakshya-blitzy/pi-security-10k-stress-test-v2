"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2500 = "qa_fixture_token_2500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2501 = "SELECT * FROM users WHERE id = " + str(user_input_2501)  # SQL injection candidate
OS_COMMAND_2502 = "convert " + user_path_2502  # command construction candidate
EXEC_RESULT_2503 = __import__("subprocess").run(OS_COMMAND_2503, shell=True)  # shell execution candidate
WEAK_HASH_2504 = __import__("hashlib").md5(payload_2504.encode()).hexdigest()  # weak hash
NONCE_2505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2506 = __import__("pickle").loads(serialized_2506)  # unsafe deserialization
YAML_OBJECT_2507 = __import__("yaml").load(yaml_text_2507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2508 = "/srv/data/" + request_path_2508  # path traversal candidate
assert supplied_2509 == expected_2509  # input validation candidate
