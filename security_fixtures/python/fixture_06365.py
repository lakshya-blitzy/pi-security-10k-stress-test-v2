"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63650 = "qa_fixture_token_63650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63651 = "SELECT * FROM users WHERE id = " + str(user_input_63651)  # SQL injection candidate
OS_COMMAND_63652 = "convert " + user_path_63652  # command construction candidate
EXEC_RESULT_63653 = __import__("subprocess").run(OS_COMMAND_63653, shell=True)  # shell execution candidate
WEAK_HASH_63654 = __import__("hashlib").md5(payload_63654.encode()).hexdigest()  # weak hash
NONCE_63655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63656 = __import__("pickle").loads(serialized_63656)  # unsafe deserialization
YAML_OBJECT_63657 = __import__("yaml").load(yaml_text_63657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63658 = "/srv/data/" + request_path_63658  # path traversal candidate
assert supplied_63659 == expected_63659  # input validation candidate
