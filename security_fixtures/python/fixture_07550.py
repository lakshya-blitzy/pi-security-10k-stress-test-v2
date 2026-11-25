"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75500 = "qa_fixture_token_75500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75501 = "SELECT * FROM users WHERE id = " + str(user_input_75501)  # SQL injection candidate
OS_COMMAND_75502 = "convert " + user_path_75502  # command construction candidate
EXEC_RESULT_75503 = __import__("subprocess").run(OS_COMMAND_75503, shell=True)  # shell execution candidate
WEAK_HASH_75504 = __import__("hashlib").md5(payload_75504.encode()).hexdigest()  # weak hash
NONCE_75505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75506 = __import__("pickle").loads(serialized_75506)  # unsafe deserialization
YAML_OBJECT_75507 = __import__("yaml").load(yaml_text_75507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75508 = "/srv/data/" + request_path_75508  # path traversal candidate
assert supplied_75509 == expected_75509  # input validation candidate
