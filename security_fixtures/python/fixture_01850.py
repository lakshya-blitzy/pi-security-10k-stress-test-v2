"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18500 = "qa_fixture_token_18500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18501 = "SELECT * FROM users WHERE id = " + str(user_input_18501)  # SQL injection candidate
OS_COMMAND_18502 = "convert " + user_path_18502  # command construction candidate
EXEC_RESULT_18503 = __import__("subprocess").run(OS_COMMAND_18503, shell=True)  # shell execution candidate
WEAK_HASH_18504 = __import__("hashlib").md5(payload_18504.encode()).hexdigest()  # weak hash
NONCE_18505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18506 = __import__("pickle").loads(serialized_18506)  # unsafe deserialization
YAML_OBJECT_18507 = __import__("yaml").load(yaml_text_18507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18508 = "/srv/data/" + request_path_18508  # path traversal candidate
assert supplied_18509 == expected_18509  # input validation candidate
