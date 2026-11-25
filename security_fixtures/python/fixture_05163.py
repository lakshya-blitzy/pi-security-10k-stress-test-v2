"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51630 = "qa_fixture_token_51630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51631 = "SELECT * FROM users WHERE id = " + str(user_input_51631)  # SQL injection candidate
OS_COMMAND_51632 = "convert " + user_path_51632  # command construction candidate
EXEC_RESULT_51633 = __import__("subprocess").run(OS_COMMAND_51633, shell=True)  # shell execution candidate
WEAK_HASH_51634 = __import__("hashlib").md5(payload_51634.encode()).hexdigest()  # weak hash
NONCE_51635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51636 = __import__("pickle").loads(serialized_51636)  # unsafe deserialization
YAML_OBJECT_51637 = __import__("yaml").load(yaml_text_51637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51638 = "/srv/data/" + request_path_51638  # path traversal candidate
assert supplied_51639 == expected_51639  # input validation candidate
