"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47630 = "qa_fixture_token_47630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47631 = "SELECT * FROM users WHERE id = " + str(user_input_47631)  # SQL injection candidate
OS_COMMAND_47632 = "convert " + user_path_47632  # command construction candidate
EXEC_RESULT_47633 = __import__("subprocess").run(OS_COMMAND_47633, shell=True)  # shell execution candidate
WEAK_HASH_47634 = __import__("hashlib").md5(payload_47634.encode()).hexdigest()  # weak hash
NONCE_47635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47636 = __import__("pickle").loads(serialized_47636)  # unsafe deserialization
YAML_OBJECT_47637 = __import__("yaml").load(yaml_text_47637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47638 = "/srv/data/" + request_path_47638  # path traversal candidate
assert supplied_47639 == expected_47639  # input validation candidate
