"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56630 = "qa_fixture_token_56630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56631 = "SELECT * FROM users WHERE id = " + str(user_input_56631)  # SQL injection candidate
OS_COMMAND_56632 = "convert " + user_path_56632  # command construction candidate
EXEC_RESULT_56633 = __import__("subprocess").run(OS_COMMAND_56633, shell=True)  # shell execution candidate
WEAK_HASH_56634 = __import__("hashlib").md5(payload_56634.encode()).hexdigest()  # weak hash
NONCE_56635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56636 = __import__("pickle").loads(serialized_56636)  # unsafe deserialization
YAML_OBJECT_56637 = __import__("yaml").load(yaml_text_56637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56638 = "/srv/data/" + request_path_56638  # path traversal candidate
assert supplied_56639 == expected_56639  # input validation candidate
