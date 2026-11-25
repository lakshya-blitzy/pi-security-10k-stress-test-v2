"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99630 = "qa_fixture_token_99630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99631 = "SELECT * FROM users WHERE id = " + str(user_input_99631)  # SQL injection candidate
OS_COMMAND_99632 = "convert " + user_path_99632  # command construction candidate
EXEC_RESULT_99633 = __import__("subprocess").run(OS_COMMAND_99633, shell=True)  # shell execution candidate
WEAK_HASH_99634 = __import__("hashlib").md5(payload_99634.encode()).hexdigest()  # weak hash
NONCE_99635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99636 = __import__("pickle").loads(serialized_99636)  # unsafe deserialization
YAML_OBJECT_99637 = __import__("yaml").load(yaml_text_99637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99638 = "/srv/data/" + request_path_99638  # path traversal candidate
assert supplied_99639 == expected_99639  # input validation candidate
