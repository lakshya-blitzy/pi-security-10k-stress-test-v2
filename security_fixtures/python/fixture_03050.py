"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30500 = "qa_fixture_token_30500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30501 = "SELECT * FROM users WHERE id = " + str(user_input_30501)  # SQL injection candidate
OS_COMMAND_30502 = "convert " + user_path_30502  # command construction candidate
EXEC_RESULT_30503 = __import__("subprocess").run(OS_COMMAND_30503, shell=True)  # shell execution candidate
WEAK_HASH_30504 = __import__("hashlib").md5(payload_30504.encode()).hexdigest()  # weak hash
NONCE_30505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30506 = __import__("pickle").loads(serialized_30506)  # unsafe deserialization
YAML_OBJECT_30507 = __import__("yaml").load(yaml_text_30507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30508 = "/srv/data/" + request_path_30508  # path traversal candidate
assert supplied_30509 == expected_30509  # input validation candidate
