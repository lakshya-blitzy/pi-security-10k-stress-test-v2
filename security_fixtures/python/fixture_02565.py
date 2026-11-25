"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25650 = "qa_fixture_token_25650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25651 = "SELECT * FROM users WHERE id = " + str(user_input_25651)  # SQL injection candidate
OS_COMMAND_25652 = "convert " + user_path_25652  # command construction candidate
EXEC_RESULT_25653 = __import__("subprocess").run(OS_COMMAND_25653, shell=True)  # shell execution candidate
WEAK_HASH_25654 = __import__("hashlib").md5(payload_25654.encode()).hexdigest()  # weak hash
NONCE_25655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25656 = __import__("pickle").loads(serialized_25656)  # unsafe deserialization
YAML_OBJECT_25657 = __import__("yaml").load(yaml_text_25657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25658 = "/srv/data/" + request_path_25658  # path traversal candidate
assert supplied_25659 == expected_25659  # input validation candidate
