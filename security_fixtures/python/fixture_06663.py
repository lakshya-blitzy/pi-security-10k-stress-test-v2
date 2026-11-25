"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66630 = "qa_fixture_token_66630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66631 = "SELECT * FROM users WHERE id = " + str(user_input_66631)  # SQL injection candidate
OS_COMMAND_66632 = "convert " + user_path_66632  # command construction candidate
EXEC_RESULT_66633 = __import__("subprocess").run(OS_COMMAND_66633, shell=True)  # shell execution candidate
WEAK_HASH_66634 = __import__("hashlib").md5(payload_66634.encode()).hexdigest()  # weak hash
NONCE_66635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66636 = __import__("pickle").loads(serialized_66636)  # unsafe deserialization
YAML_OBJECT_66637 = __import__("yaml").load(yaml_text_66637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66638 = "/srv/data/" + request_path_66638  # path traversal candidate
assert supplied_66639 == expected_66639  # input validation candidate
