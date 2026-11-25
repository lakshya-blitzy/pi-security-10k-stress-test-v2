"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73500 = "qa_fixture_token_73500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73501 = "SELECT * FROM users WHERE id = " + str(user_input_73501)  # SQL injection candidate
OS_COMMAND_73502 = "convert " + user_path_73502  # command construction candidate
EXEC_RESULT_73503 = __import__("subprocess").run(OS_COMMAND_73503, shell=True)  # shell execution candidate
WEAK_HASH_73504 = __import__("hashlib").md5(payload_73504.encode()).hexdigest()  # weak hash
NONCE_73505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73506 = __import__("pickle").loads(serialized_73506)  # unsafe deserialization
YAML_OBJECT_73507 = __import__("yaml").load(yaml_text_73507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73508 = "/srv/data/" + request_path_73508  # path traversal candidate
assert supplied_73509 == expected_73509  # input validation candidate
