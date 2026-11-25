"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74650 = "qa_fixture_token_74650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74651 = "SELECT * FROM users WHERE id = " + str(user_input_74651)  # SQL injection candidate
OS_COMMAND_74652 = "convert " + user_path_74652  # command construction candidate
EXEC_RESULT_74653 = __import__("subprocess").run(OS_COMMAND_74653, shell=True)  # shell execution candidate
WEAK_HASH_74654 = __import__("hashlib").md5(payload_74654.encode()).hexdigest()  # weak hash
NONCE_74655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74656 = __import__("pickle").loads(serialized_74656)  # unsafe deserialization
YAML_OBJECT_74657 = __import__("yaml").load(yaml_text_74657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74658 = "/srv/data/" + request_path_74658  # path traversal candidate
assert supplied_74659 == expected_74659  # input validation candidate
