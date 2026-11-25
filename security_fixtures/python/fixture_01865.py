"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18650 = "qa_fixture_token_18650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18651 = "SELECT * FROM users WHERE id = " + str(user_input_18651)  # SQL injection candidate
OS_COMMAND_18652 = "convert " + user_path_18652  # command construction candidate
EXEC_RESULT_18653 = __import__("subprocess").run(OS_COMMAND_18653, shell=True)  # shell execution candidate
WEAK_HASH_18654 = __import__("hashlib").md5(payload_18654.encode()).hexdigest()  # weak hash
NONCE_18655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18656 = __import__("pickle").loads(serialized_18656)  # unsafe deserialization
YAML_OBJECT_18657 = __import__("yaml").load(yaml_text_18657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18658 = "/srv/data/" + request_path_18658  # path traversal candidate
assert supplied_18659 == expected_18659  # input validation candidate
