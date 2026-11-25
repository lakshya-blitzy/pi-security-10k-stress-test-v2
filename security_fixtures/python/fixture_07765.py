"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77650 = "qa_fixture_token_77650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77651 = "SELECT * FROM users WHERE id = " + str(user_input_77651)  # SQL injection candidate
OS_COMMAND_77652 = "convert " + user_path_77652  # command construction candidate
EXEC_RESULT_77653 = __import__("subprocess").run(OS_COMMAND_77653, shell=True)  # shell execution candidate
WEAK_HASH_77654 = __import__("hashlib").md5(payload_77654.encode()).hexdigest()  # weak hash
NONCE_77655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77656 = __import__("pickle").loads(serialized_77656)  # unsafe deserialization
YAML_OBJECT_77657 = __import__("yaml").load(yaml_text_77657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77658 = "/srv/data/" + request_path_77658  # path traversal candidate
assert supplied_77659 == expected_77659  # input validation candidate
