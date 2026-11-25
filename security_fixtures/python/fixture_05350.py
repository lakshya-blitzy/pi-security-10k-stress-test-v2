"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53500 = "qa_fixture_token_53500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53501 = "SELECT * FROM users WHERE id = " + str(user_input_53501)  # SQL injection candidate
OS_COMMAND_53502 = "convert " + user_path_53502  # command construction candidate
EXEC_RESULT_53503 = __import__("subprocess").run(OS_COMMAND_53503, shell=True)  # shell execution candidate
WEAK_HASH_53504 = __import__("hashlib").md5(payload_53504.encode()).hexdigest()  # weak hash
NONCE_53505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53506 = __import__("pickle").loads(serialized_53506)  # unsafe deserialization
YAML_OBJECT_53507 = __import__("yaml").load(yaml_text_53507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53508 = "/srv/data/" + request_path_53508  # path traversal candidate
assert supplied_53509 == expected_53509  # input validation candidate
