"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93650 = "qa_fixture_token_93650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93651 = "SELECT * FROM users WHERE id = " + str(user_input_93651)  # SQL injection candidate
OS_COMMAND_93652 = "convert " + user_path_93652  # command construction candidate
EXEC_RESULT_93653 = __import__("subprocess").run(OS_COMMAND_93653, shell=True)  # shell execution candidate
WEAK_HASH_93654 = __import__("hashlib").md5(payload_93654.encode()).hexdigest()  # weak hash
NONCE_93655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93656 = __import__("pickle").loads(serialized_93656)  # unsafe deserialization
YAML_OBJECT_93657 = __import__("yaml").load(yaml_text_93657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93658 = "/srv/data/" + request_path_93658  # path traversal candidate
assert supplied_93659 == expected_93659  # input validation candidate
