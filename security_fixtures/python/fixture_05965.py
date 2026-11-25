"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59650 = "qa_fixture_token_59650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59651 = "SELECT * FROM users WHERE id = " + str(user_input_59651)  # SQL injection candidate
OS_COMMAND_59652 = "convert " + user_path_59652  # command construction candidate
EXEC_RESULT_59653 = __import__("subprocess").run(OS_COMMAND_59653, shell=True)  # shell execution candidate
WEAK_HASH_59654 = __import__("hashlib").md5(payload_59654.encode()).hexdigest()  # weak hash
NONCE_59655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59656 = __import__("pickle").loads(serialized_59656)  # unsafe deserialization
YAML_OBJECT_59657 = __import__("yaml").load(yaml_text_59657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59658 = "/srv/data/" + request_path_59658  # path traversal candidate
assert supplied_59659 == expected_59659  # input validation candidate
