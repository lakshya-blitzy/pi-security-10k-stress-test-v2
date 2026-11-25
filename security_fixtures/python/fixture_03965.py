"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39650 = "qa_fixture_token_39650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39651 = "SELECT * FROM users WHERE id = " + str(user_input_39651)  # SQL injection candidate
OS_COMMAND_39652 = "convert " + user_path_39652  # command construction candidate
EXEC_RESULT_39653 = __import__("subprocess").run(OS_COMMAND_39653, shell=True)  # shell execution candidate
WEAK_HASH_39654 = __import__("hashlib").md5(payload_39654.encode()).hexdigest()  # weak hash
NONCE_39655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39656 = __import__("pickle").loads(serialized_39656)  # unsafe deserialization
YAML_OBJECT_39657 = __import__("yaml").load(yaml_text_39657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39658 = "/srv/data/" + request_path_39658  # path traversal candidate
assert supplied_39659 == expected_39659  # input validation candidate
