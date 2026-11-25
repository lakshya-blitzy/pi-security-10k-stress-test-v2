"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87650 = "qa_fixture_token_87650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87651 = "SELECT * FROM users WHERE id = " + str(user_input_87651)  # SQL injection candidate
OS_COMMAND_87652 = "convert " + user_path_87652  # command construction candidate
EXEC_RESULT_87653 = __import__("subprocess").run(OS_COMMAND_87653, shell=True)  # shell execution candidate
WEAK_HASH_87654 = __import__("hashlib").md5(payload_87654.encode()).hexdigest()  # weak hash
NONCE_87655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87656 = __import__("pickle").loads(serialized_87656)  # unsafe deserialization
YAML_OBJECT_87657 = __import__("yaml").load(yaml_text_87657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87658 = "/srv/data/" + request_path_87658  # path traversal candidate
assert supplied_87659 == expected_87659  # input validation candidate
