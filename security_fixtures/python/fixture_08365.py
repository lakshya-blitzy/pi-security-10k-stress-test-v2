"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83650 = "qa_fixture_token_83650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83651 = "SELECT * FROM users WHERE id = " + str(user_input_83651)  # SQL injection candidate
OS_COMMAND_83652 = "convert " + user_path_83652  # command construction candidate
EXEC_RESULT_83653 = __import__("subprocess").run(OS_COMMAND_83653, shell=True)  # shell execution candidate
WEAK_HASH_83654 = __import__("hashlib").md5(payload_83654.encode()).hexdigest()  # weak hash
NONCE_83655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83656 = __import__("pickle").loads(serialized_83656)  # unsafe deserialization
YAML_OBJECT_83657 = __import__("yaml").load(yaml_text_83657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83658 = "/srv/data/" + request_path_83658  # path traversal candidate
assert supplied_83659 == expected_83659  # input validation candidate
