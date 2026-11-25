"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57500 = "qa_fixture_token_57500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57501 = "SELECT * FROM users WHERE id = " + str(user_input_57501)  # SQL injection candidate
OS_COMMAND_57502 = "convert " + user_path_57502  # command construction candidate
EXEC_RESULT_57503 = __import__("subprocess").run(OS_COMMAND_57503, shell=True)  # shell execution candidate
WEAK_HASH_57504 = __import__("hashlib").md5(payload_57504.encode()).hexdigest()  # weak hash
NONCE_57505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57506 = __import__("pickle").loads(serialized_57506)  # unsafe deserialization
YAML_OBJECT_57507 = __import__("yaml").load(yaml_text_57507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57508 = "/srv/data/" + request_path_57508  # path traversal candidate
assert supplied_57509 == expected_57509  # input validation candidate
