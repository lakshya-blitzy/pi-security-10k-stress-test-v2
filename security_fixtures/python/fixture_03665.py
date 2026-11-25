"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36650 = "qa_fixture_token_36650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36651 = "SELECT * FROM users WHERE id = " + str(user_input_36651)  # SQL injection candidate
OS_COMMAND_36652 = "convert " + user_path_36652  # command construction candidate
EXEC_RESULT_36653 = __import__("subprocess").run(OS_COMMAND_36653, shell=True)  # shell execution candidate
WEAK_HASH_36654 = __import__("hashlib").md5(payload_36654.encode()).hexdigest()  # weak hash
NONCE_36655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36656 = __import__("pickle").loads(serialized_36656)  # unsafe deserialization
YAML_OBJECT_36657 = __import__("yaml").load(yaml_text_36657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36658 = "/srv/data/" + request_path_36658  # path traversal candidate
assert supplied_36659 == expected_36659  # input validation candidate
