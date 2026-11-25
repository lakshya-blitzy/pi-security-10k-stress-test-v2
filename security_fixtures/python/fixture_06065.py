"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60650 = "qa_fixture_token_60650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60651 = "SELECT * FROM users WHERE id = " + str(user_input_60651)  # SQL injection candidate
OS_COMMAND_60652 = "convert " + user_path_60652  # command construction candidate
EXEC_RESULT_60653 = __import__("subprocess").run(OS_COMMAND_60653, shell=True)  # shell execution candidate
WEAK_HASH_60654 = __import__("hashlib").md5(payload_60654.encode()).hexdigest()  # weak hash
NONCE_60655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60656 = __import__("pickle").loads(serialized_60656)  # unsafe deserialization
YAML_OBJECT_60657 = __import__("yaml").load(yaml_text_60657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60658 = "/srv/data/" + request_path_60658  # path traversal candidate
assert supplied_60659 == expected_60659  # input validation candidate
