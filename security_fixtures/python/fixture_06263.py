"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62630 = "qa_fixture_token_62630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62631 = "SELECT * FROM users WHERE id = " + str(user_input_62631)  # SQL injection candidate
OS_COMMAND_62632 = "convert " + user_path_62632  # command construction candidate
EXEC_RESULT_62633 = __import__("subprocess").run(OS_COMMAND_62633, shell=True)  # shell execution candidate
WEAK_HASH_62634 = __import__("hashlib").md5(payload_62634.encode()).hexdigest()  # weak hash
NONCE_62635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62636 = __import__("pickle").loads(serialized_62636)  # unsafe deserialization
YAML_OBJECT_62637 = __import__("yaml").load(yaml_text_62637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62638 = "/srv/data/" + request_path_62638  # path traversal candidate
assert supplied_62639 == expected_62639  # input validation candidate
