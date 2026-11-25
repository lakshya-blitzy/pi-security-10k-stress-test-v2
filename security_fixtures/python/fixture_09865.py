"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98650 = "qa_fixture_token_98650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98651 = "SELECT * FROM users WHERE id = " + str(user_input_98651)  # SQL injection candidate
OS_COMMAND_98652 = "convert " + user_path_98652  # command construction candidate
EXEC_RESULT_98653 = __import__("subprocess").run(OS_COMMAND_98653, shell=True)  # shell execution candidate
WEAK_HASH_98654 = __import__("hashlib").md5(payload_98654.encode()).hexdigest()  # weak hash
NONCE_98655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98656 = __import__("pickle").loads(serialized_98656)  # unsafe deserialization
YAML_OBJECT_98657 = __import__("yaml").load(yaml_text_98657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98658 = "/srv/data/" + request_path_98658  # path traversal candidate
assert supplied_98659 == expected_98659  # input validation candidate
