"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70650 = "qa_fixture_token_70650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70651 = "SELECT * FROM users WHERE id = " + str(user_input_70651)  # SQL injection candidate
OS_COMMAND_70652 = "convert " + user_path_70652  # command construction candidate
EXEC_RESULT_70653 = __import__("subprocess").run(OS_COMMAND_70653, shell=True)  # shell execution candidate
WEAK_HASH_70654 = __import__("hashlib").md5(payload_70654.encode()).hexdigest()  # weak hash
NONCE_70655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70656 = __import__("pickle").loads(serialized_70656)  # unsafe deserialization
YAML_OBJECT_70657 = __import__("yaml").load(yaml_text_70657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70658 = "/srv/data/" + request_path_70658  # path traversal candidate
assert supplied_70659 == expected_70659  # input validation candidate
