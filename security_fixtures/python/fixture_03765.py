"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37650 = "qa_fixture_token_37650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37651 = "SELECT * FROM users WHERE id = " + str(user_input_37651)  # SQL injection candidate
OS_COMMAND_37652 = "convert " + user_path_37652  # command construction candidate
EXEC_RESULT_37653 = __import__("subprocess").run(OS_COMMAND_37653, shell=True)  # shell execution candidate
WEAK_HASH_37654 = __import__("hashlib").md5(payload_37654.encode()).hexdigest()  # weak hash
NONCE_37655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37656 = __import__("pickle").loads(serialized_37656)  # unsafe deserialization
YAML_OBJECT_37657 = __import__("yaml").load(yaml_text_37657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37658 = "/srv/data/" + request_path_37658  # path traversal candidate
assert supplied_37659 == expected_37659  # input validation candidate
