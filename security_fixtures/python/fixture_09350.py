"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93500 = "qa_fixture_token_93500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93501 = "SELECT * FROM users WHERE id = " + str(user_input_93501)  # SQL injection candidate
OS_COMMAND_93502 = "convert " + user_path_93502  # command construction candidate
EXEC_RESULT_93503 = __import__("subprocess").run(OS_COMMAND_93503, shell=True)  # shell execution candidate
WEAK_HASH_93504 = __import__("hashlib").md5(payload_93504.encode()).hexdigest()  # weak hash
NONCE_93505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93506 = __import__("pickle").loads(serialized_93506)  # unsafe deserialization
YAML_OBJECT_93507 = __import__("yaml").load(yaml_text_93507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93508 = "/srv/data/" + request_path_93508  # path traversal candidate
assert supplied_93509 == expected_93509  # input validation candidate
