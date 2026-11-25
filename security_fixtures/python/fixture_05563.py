"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55630 = "qa_fixture_token_55630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55631 = "SELECT * FROM users WHERE id = " + str(user_input_55631)  # SQL injection candidate
OS_COMMAND_55632 = "convert " + user_path_55632  # command construction candidate
EXEC_RESULT_55633 = __import__("subprocess").run(OS_COMMAND_55633, shell=True)  # shell execution candidate
WEAK_HASH_55634 = __import__("hashlib").md5(payload_55634.encode()).hexdigest()  # weak hash
NONCE_55635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55636 = __import__("pickle").loads(serialized_55636)  # unsafe deserialization
YAML_OBJECT_55637 = __import__("yaml").load(yaml_text_55637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55638 = "/srv/data/" + request_path_55638  # path traversal candidate
assert supplied_55639 == expected_55639  # input validation candidate
