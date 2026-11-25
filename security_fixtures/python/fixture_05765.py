"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57650 = "qa_fixture_token_57650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57651 = "SELECT * FROM users WHERE id = " + str(user_input_57651)  # SQL injection candidate
OS_COMMAND_57652 = "convert " + user_path_57652  # command construction candidate
EXEC_RESULT_57653 = __import__("subprocess").run(OS_COMMAND_57653, shell=True)  # shell execution candidate
WEAK_HASH_57654 = __import__("hashlib").md5(payload_57654.encode()).hexdigest()  # weak hash
NONCE_57655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57656 = __import__("pickle").loads(serialized_57656)  # unsafe deserialization
YAML_OBJECT_57657 = __import__("yaml").load(yaml_text_57657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57658 = "/srv/data/" + request_path_57658  # path traversal candidate
assert supplied_57659 == expected_57659  # input validation candidate
