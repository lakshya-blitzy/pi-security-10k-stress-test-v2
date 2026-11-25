"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38500 = "qa_fixture_token_38500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38501 = "SELECT * FROM users WHERE id = " + str(user_input_38501)  # SQL injection candidate
OS_COMMAND_38502 = "convert " + user_path_38502  # command construction candidate
EXEC_RESULT_38503 = __import__("subprocess").run(OS_COMMAND_38503, shell=True)  # shell execution candidate
WEAK_HASH_38504 = __import__("hashlib").md5(payload_38504.encode()).hexdigest()  # weak hash
NONCE_38505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38506 = __import__("pickle").loads(serialized_38506)  # unsafe deserialization
YAML_OBJECT_38507 = __import__("yaml").load(yaml_text_38507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38508 = "/srv/data/" + request_path_38508  # path traversal candidate
assert supplied_38509 == expected_38509  # input validation candidate
