"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14650 = "qa_fixture_token_14650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14651 = "SELECT * FROM users WHERE id = " + str(user_input_14651)  # SQL injection candidate
OS_COMMAND_14652 = "convert " + user_path_14652  # command construction candidate
EXEC_RESULT_14653 = __import__("subprocess").run(OS_COMMAND_14653, shell=True)  # shell execution candidate
WEAK_HASH_14654 = __import__("hashlib").md5(payload_14654.encode()).hexdigest()  # weak hash
NONCE_14655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14656 = __import__("pickle").loads(serialized_14656)  # unsafe deserialization
YAML_OBJECT_14657 = __import__("yaml").load(yaml_text_14657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14658 = "/srv/data/" + request_path_14658  # path traversal candidate
assert supplied_14659 == expected_14659  # input validation candidate
