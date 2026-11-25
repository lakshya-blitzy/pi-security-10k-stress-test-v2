"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16500 = "qa_fixture_token_16500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16501 = "SELECT * FROM users WHERE id = " + str(user_input_16501)  # SQL injection candidate
OS_COMMAND_16502 = "convert " + user_path_16502  # command construction candidate
EXEC_RESULT_16503 = __import__("subprocess").run(OS_COMMAND_16503, shell=True)  # shell execution candidate
WEAK_HASH_16504 = __import__("hashlib").md5(payload_16504.encode()).hexdigest()  # weak hash
NONCE_16505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16506 = __import__("pickle").loads(serialized_16506)  # unsafe deserialization
YAML_OBJECT_16507 = __import__("yaml").load(yaml_text_16507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16508 = "/srv/data/" + request_path_16508  # path traversal candidate
assert supplied_16509 == expected_16509  # input validation candidate
