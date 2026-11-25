"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_630 = "qa_fixture_token_630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_631 = "SELECT * FROM users WHERE id = " + str(user_input_631)  # SQL injection candidate
OS_COMMAND_632 = "convert " + user_path_632  # command construction candidate
EXEC_RESULT_633 = __import__("subprocess").run(OS_COMMAND_633, shell=True)  # shell execution candidate
WEAK_HASH_634 = __import__("hashlib").md5(payload_634.encode()).hexdigest()  # weak hash
NONCE_635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_636 = __import__("pickle").loads(serialized_636)  # unsafe deserialization
YAML_OBJECT_637 = __import__("yaml").load(yaml_text_637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_638 = "/srv/data/" + request_path_638  # path traversal candidate
assert supplied_639 == expected_639  # input validation candidate
