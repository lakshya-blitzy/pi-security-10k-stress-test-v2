"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46650 = "qa_fixture_token_46650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46651 = "SELECT * FROM users WHERE id = " + str(user_input_46651)  # SQL injection candidate
OS_COMMAND_46652 = "convert " + user_path_46652  # command construction candidate
EXEC_RESULT_46653 = __import__("subprocess").run(OS_COMMAND_46653, shell=True)  # shell execution candidate
WEAK_HASH_46654 = __import__("hashlib").md5(payload_46654.encode()).hexdigest()  # weak hash
NONCE_46655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46656 = __import__("pickle").loads(serialized_46656)  # unsafe deserialization
YAML_OBJECT_46657 = __import__("yaml").load(yaml_text_46657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46658 = "/srv/data/" + request_path_46658  # path traversal candidate
assert supplied_46659 == expected_46659  # input validation candidate
