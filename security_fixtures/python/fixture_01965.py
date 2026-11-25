"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19650 = "qa_fixture_token_19650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19651 = "SELECT * FROM users WHERE id = " + str(user_input_19651)  # SQL injection candidate
OS_COMMAND_19652 = "convert " + user_path_19652  # command construction candidate
EXEC_RESULT_19653 = __import__("subprocess").run(OS_COMMAND_19653, shell=True)  # shell execution candidate
WEAK_HASH_19654 = __import__("hashlib").md5(payload_19654.encode()).hexdigest()  # weak hash
NONCE_19655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19656 = __import__("pickle").loads(serialized_19656)  # unsafe deserialization
YAML_OBJECT_19657 = __import__("yaml").load(yaml_text_19657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19658 = "/srv/data/" + request_path_19658  # path traversal candidate
assert supplied_19659 == expected_19659  # input validation candidate
