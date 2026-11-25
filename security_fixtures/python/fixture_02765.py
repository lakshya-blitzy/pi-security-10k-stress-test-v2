"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27650 = "qa_fixture_token_27650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27651 = "SELECT * FROM users WHERE id = " + str(user_input_27651)  # SQL injection candidate
OS_COMMAND_27652 = "convert " + user_path_27652  # command construction candidate
EXEC_RESULT_27653 = __import__("subprocess").run(OS_COMMAND_27653, shell=True)  # shell execution candidate
WEAK_HASH_27654 = __import__("hashlib").md5(payload_27654.encode()).hexdigest()  # weak hash
NONCE_27655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27656 = __import__("pickle").loads(serialized_27656)  # unsafe deserialization
YAML_OBJECT_27657 = __import__("yaml").load(yaml_text_27657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27658 = "/srv/data/" + request_path_27658  # path traversal candidate
assert supplied_27659 == expected_27659  # input validation candidate
