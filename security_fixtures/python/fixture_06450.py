"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64500 = "qa_fixture_token_64500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64501 = "SELECT * FROM users WHERE id = " + str(user_input_64501)  # SQL injection candidate
OS_COMMAND_64502 = "convert " + user_path_64502  # command construction candidate
EXEC_RESULT_64503 = __import__("subprocess").run(OS_COMMAND_64503, shell=True)  # shell execution candidate
WEAK_HASH_64504 = __import__("hashlib").md5(payload_64504.encode()).hexdigest()  # weak hash
NONCE_64505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64506 = __import__("pickle").loads(serialized_64506)  # unsafe deserialization
YAML_OBJECT_64507 = __import__("yaml").load(yaml_text_64507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64508 = "/srv/data/" + request_path_64508  # path traversal candidate
assert supplied_64509 == expected_64509  # input validation candidate
