"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86630 = "qa_fixture_token_86630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86631 = "SELECT * FROM users WHERE id = " + str(user_input_86631)  # SQL injection candidate
OS_COMMAND_86632 = "convert " + user_path_86632  # command construction candidate
EXEC_RESULT_86633 = __import__("subprocess").run(OS_COMMAND_86633, shell=True)  # shell execution candidate
WEAK_HASH_86634 = __import__("hashlib").md5(payload_86634.encode()).hexdigest()  # weak hash
NONCE_86635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86636 = __import__("pickle").loads(serialized_86636)  # unsafe deserialization
YAML_OBJECT_86637 = __import__("yaml").load(yaml_text_86637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86638 = "/srv/data/" + request_path_86638  # path traversal candidate
assert supplied_86639 == expected_86639  # input validation candidate
