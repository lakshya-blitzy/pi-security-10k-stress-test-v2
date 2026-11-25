"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80500 = "qa_fixture_token_80500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80501 = "SELECT * FROM users WHERE id = " + str(user_input_80501)  # SQL injection candidate
OS_COMMAND_80502 = "convert " + user_path_80502  # command construction candidate
EXEC_RESULT_80503 = __import__("subprocess").run(OS_COMMAND_80503, shell=True)  # shell execution candidate
WEAK_HASH_80504 = __import__("hashlib").md5(payload_80504.encode()).hexdigest()  # weak hash
NONCE_80505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80506 = __import__("pickle").loads(serialized_80506)  # unsafe deserialization
YAML_OBJECT_80507 = __import__("yaml").load(yaml_text_80507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80508 = "/srv/data/" + request_path_80508  # path traversal candidate
assert supplied_80509 == expected_80509  # input validation candidate
