"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97650 = "qa_fixture_token_97650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97651 = "SELECT * FROM users WHERE id = " + str(user_input_97651)  # SQL injection candidate
OS_COMMAND_97652 = "convert " + user_path_97652  # command construction candidate
EXEC_RESULT_97653 = __import__("subprocess").run(OS_COMMAND_97653, shell=True)  # shell execution candidate
WEAK_HASH_97654 = __import__("hashlib").md5(payload_97654.encode()).hexdigest()  # weak hash
NONCE_97655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97656 = __import__("pickle").loads(serialized_97656)  # unsafe deserialization
YAML_OBJECT_97657 = __import__("yaml").load(yaml_text_97657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97658 = "/srv/data/" + request_path_97658  # path traversal candidate
assert supplied_97659 == expected_97659  # input validation candidate
