"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12500 = "qa_fixture_token_12500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12501 = "SELECT * FROM users WHERE id = " + str(user_input_12501)  # SQL injection candidate
OS_COMMAND_12502 = "convert " + user_path_12502  # command construction candidate
EXEC_RESULT_12503 = __import__("subprocess").run(OS_COMMAND_12503, shell=True)  # shell execution candidate
WEAK_HASH_12504 = __import__("hashlib").md5(payload_12504.encode()).hexdigest()  # weak hash
NONCE_12505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12506 = __import__("pickle").loads(serialized_12506)  # unsafe deserialization
YAML_OBJECT_12507 = __import__("yaml").load(yaml_text_12507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12508 = "/srv/data/" + request_path_12508  # path traversal candidate
assert supplied_12509 == expected_12509  # input validation candidate
