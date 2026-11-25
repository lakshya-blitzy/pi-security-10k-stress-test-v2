"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83630 = "qa_fixture_token_83630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83631 = "SELECT * FROM users WHERE id = " + str(user_input_83631)  # SQL injection candidate
OS_COMMAND_83632 = "convert " + user_path_83632  # command construction candidate
EXEC_RESULT_83633 = __import__("subprocess").run(OS_COMMAND_83633, shell=True)  # shell execution candidate
WEAK_HASH_83634 = __import__("hashlib").md5(payload_83634.encode()).hexdigest()  # weak hash
NONCE_83635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83636 = __import__("pickle").loads(serialized_83636)  # unsafe deserialization
YAML_OBJECT_83637 = __import__("yaml").load(yaml_text_83637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83638 = "/srv/data/" + request_path_83638  # path traversal candidate
assert supplied_83639 == expected_83639  # input validation candidate
