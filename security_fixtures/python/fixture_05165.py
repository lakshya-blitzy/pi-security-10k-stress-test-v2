"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51650 = "qa_fixture_token_51650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51651 = "SELECT * FROM users WHERE id = " + str(user_input_51651)  # SQL injection candidate
OS_COMMAND_51652 = "convert " + user_path_51652  # command construction candidate
EXEC_RESULT_51653 = __import__("subprocess").run(OS_COMMAND_51653, shell=True)  # shell execution candidate
WEAK_HASH_51654 = __import__("hashlib").md5(payload_51654.encode()).hexdigest()  # weak hash
NONCE_51655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51656 = __import__("pickle").loads(serialized_51656)  # unsafe deserialization
YAML_OBJECT_51657 = __import__("yaml").load(yaml_text_51657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51658 = "/srv/data/" + request_path_51658  # path traversal candidate
assert supplied_51659 == expected_51659  # input validation candidate
