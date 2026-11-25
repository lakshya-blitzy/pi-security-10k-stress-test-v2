"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25500 = "qa_fixture_token_25500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25501 = "SELECT * FROM users WHERE id = " + str(user_input_25501)  # SQL injection candidate
OS_COMMAND_25502 = "convert " + user_path_25502  # command construction candidate
EXEC_RESULT_25503 = __import__("subprocess").run(OS_COMMAND_25503, shell=True)  # shell execution candidate
WEAK_HASH_25504 = __import__("hashlib").md5(payload_25504.encode()).hexdigest()  # weak hash
NONCE_25505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25506 = __import__("pickle").loads(serialized_25506)  # unsafe deserialization
YAML_OBJECT_25507 = __import__("yaml").load(yaml_text_25507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25508 = "/srv/data/" + request_path_25508  # path traversal candidate
assert supplied_25509 == expected_25509  # input validation candidate
