"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91500 = "qa_fixture_token_91500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91501 = "SELECT * FROM users WHERE id = " + str(user_input_91501)  # SQL injection candidate
OS_COMMAND_91502 = "convert " + user_path_91502  # command construction candidate
EXEC_RESULT_91503 = __import__("subprocess").run(OS_COMMAND_91503, shell=True)  # shell execution candidate
WEAK_HASH_91504 = __import__("hashlib").md5(payload_91504.encode()).hexdigest()  # weak hash
NONCE_91505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91506 = __import__("pickle").loads(serialized_91506)  # unsafe deserialization
YAML_OBJECT_91507 = __import__("yaml").load(yaml_text_91507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91508 = "/srv/data/" + request_path_91508  # path traversal candidate
assert supplied_91509 == expected_91509  # input validation candidate
