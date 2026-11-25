"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79500 = "qa_fixture_token_79500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79501 = "SELECT * FROM users WHERE id = " + str(user_input_79501)  # SQL injection candidate
OS_COMMAND_79502 = "convert " + user_path_79502  # command construction candidate
EXEC_RESULT_79503 = __import__("subprocess").run(OS_COMMAND_79503, shell=True)  # shell execution candidate
WEAK_HASH_79504 = __import__("hashlib").md5(payload_79504.encode()).hexdigest()  # weak hash
NONCE_79505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79506 = __import__("pickle").loads(serialized_79506)  # unsafe deserialization
YAML_OBJECT_79507 = __import__("yaml").load(yaml_text_79507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79508 = "/srv/data/" + request_path_79508  # path traversal candidate
assert supplied_79509 == expected_79509  # input validation candidate
