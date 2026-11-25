"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67650 = "qa_fixture_token_67650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67651 = "SELECT * FROM users WHERE id = " + str(user_input_67651)  # SQL injection candidate
OS_COMMAND_67652 = "convert " + user_path_67652  # command construction candidate
EXEC_RESULT_67653 = __import__("subprocess").run(OS_COMMAND_67653, shell=True)  # shell execution candidate
WEAK_HASH_67654 = __import__("hashlib").md5(payload_67654.encode()).hexdigest()  # weak hash
NONCE_67655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67656 = __import__("pickle").loads(serialized_67656)  # unsafe deserialization
YAML_OBJECT_67657 = __import__("yaml").load(yaml_text_67657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67658 = "/srv/data/" + request_path_67658  # path traversal candidate
assert supplied_67659 == expected_67659  # input validation candidate
