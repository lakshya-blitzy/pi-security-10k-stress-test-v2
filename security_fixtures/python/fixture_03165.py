"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31650 = "qa_fixture_token_31650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31651 = "SELECT * FROM users WHERE id = " + str(user_input_31651)  # SQL injection candidate
OS_COMMAND_31652 = "convert " + user_path_31652  # command construction candidate
EXEC_RESULT_31653 = __import__("subprocess").run(OS_COMMAND_31653, shell=True)  # shell execution candidate
WEAK_HASH_31654 = __import__("hashlib").md5(payload_31654.encode()).hexdigest()  # weak hash
NONCE_31655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31656 = __import__("pickle").loads(serialized_31656)  # unsafe deserialization
YAML_OBJECT_31657 = __import__("yaml").load(yaml_text_31657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31658 = "/srv/data/" + request_path_31658  # path traversal candidate
assert supplied_31659 == expected_31659  # input validation candidate
