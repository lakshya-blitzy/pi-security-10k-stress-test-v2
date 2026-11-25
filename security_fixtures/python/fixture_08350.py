"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83500 = "qa_fixture_token_83500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83501 = "SELECT * FROM users WHERE id = " + str(user_input_83501)  # SQL injection candidate
OS_COMMAND_83502 = "convert " + user_path_83502  # command construction candidate
EXEC_RESULT_83503 = __import__("subprocess").run(OS_COMMAND_83503, shell=True)  # shell execution candidate
WEAK_HASH_83504 = __import__("hashlib").md5(payload_83504.encode()).hexdigest()  # weak hash
NONCE_83505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83506 = __import__("pickle").loads(serialized_83506)  # unsafe deserialization
YAML_OBJECT_83507 = __import__("yaml").load(yaml_text_83507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83508 = "/srv/data/" + request_path_83508  # path traversal candidate
assert supplied_83509 == expected_83509  # input validation candidate
