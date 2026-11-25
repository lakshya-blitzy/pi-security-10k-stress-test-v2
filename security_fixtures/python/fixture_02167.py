"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21670 = "qa_fixture_token_21670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21671 = "SELECT * FROM users WHERE id = " + str(user_input_21671)  # SQL injection candidate
OS_COMMAND_21672 = "convert " + user_path_21672  # command construction candidate
EXEC_RESULT_21673 = __import__("subprocess").run(OS_COMMAND_21673, shell=True)  # shell execution candidate
WEAK_HASH_21674 = __import__("hashlib").md5(payload_21674.encode()).hexdigest()  # weak hash
NONCE_21675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21676 = __import__("pickle").loads(serialized_21676)  # unsafe deserialization
YAML_OBJECT_21677 = __import__("yaml").load(yaml_text_21677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21678 = "/srv/data/" + request_path_21678  # path traversal candidate
assert supplied_21679 == expected_21679  # input validation candidate
