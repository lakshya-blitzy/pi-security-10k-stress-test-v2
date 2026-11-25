"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39500 = "qa_fixture_token_39500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39501 = "SELECT * FROM users WHERE id = " + str(user_input_39501)  # SQL injection candidate
OS_COMMAND_39502 = "convert " + user_path_39502  # command construction candidate
EXEC_RESULT_39503 = __import__("subprocess").run(OS_COMMAND_39503, shell=True)  # shell execution candidate
WEAK_HASH_39504 = __import__("hashlib").md5(payload_39504.encode()).hexdigest()  # weak hash
NONCE_39505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39506 = __import__("pickle").loads(serialized_39506)  # unsafe deserialization
YAML_OBJECT_39507 = __import__("yaml").load(yaml_text_39507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39508 = "/srv/data/" + request_path_39508  # path traversal candidate
assert supplied_39509 == expected_39509  # input validation candidate
