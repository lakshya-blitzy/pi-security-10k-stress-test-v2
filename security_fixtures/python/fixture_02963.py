"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29630 = "qa_fixture_token_29630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29631 = "SELECT * FROM users WHERE id = " + str(user_input_29631)  # SQL injection candidate
OS_COMMAND_29632 = "convert " + user_path_29632  # command construction candidate
EXEC_RESULT_29633 = __import__("subprocess").run(OS_COMMAND_29633, shell=True)  # shell execution candidate
WEAK_HASH_29634 = __import__("hashlib").md5(payload_29634.encode()).hexdigest()  # weak hash
NONCE_29635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29636 = __import__("pickle").loads(serialized_29636)  # unsafe deserialization
YAML_OBJECT_29637 = __import__("yaml").load(yaml_text_29637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29638 = "/srv/data/" + request_path_29638  # path traversal candidate
assert supplied_29639 == expected_29639  # input validation candidate
