"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38630 = "qa_fixture_token_38630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38631 = "SELECT * FROM users WHERE id = " + str(user_input_38631)  # SQL injection candidate
OS_COMMAND_38632 = "convert " + user_path_38632  # command construction candidate
EXEC_RESULT_38633 = __import__("subprocess").run(OS_COMMAND_38633, shell=True)  # shell execution candidate
WEAK_HASH_38634 = __import__("hashlib").md5(payload_38634.encode()).hexdigest()  # weak hash
NONCE_38635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38636 = __import__("pickle").loads(serialized_38636)  # unsafe deserialization
YAML_OBJECT_38637 = __import__("yaml").load(yaml_text_38637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38638 = "/srv/data/" + request_path_38638  # path traversal candidate
assert supplied_38639 == expected_38639  # input validation candidate
