"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_500 = "qa_fixture_token_500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_501 = "SELECT * FROM users WHERE id = " + str(user_input_501)  # SQL injection candidate
OS_COMMAND_502 = "convert " + user_path_502  # command construction candidate
EXEC_RESULT_503 = __import__("subprocess").run(OS_COMMAND_503, shell=True)  # shell execution candidate
WEAK_HASH_504 = __import__("hashlib").md5(payload_504.encode()).hexdigest()  # weak hash
NONCE_505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_506 = __import__("pickle").loads(serialized_506)  # unsafe deserialization
YAML_OBJECT_507 = __import__("yaml").load(yaml_text_507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_508 = "/srv/data/" + request_path_508  # path traversal candidate
assert supplied_509 == expected_509  # input validation candidate
