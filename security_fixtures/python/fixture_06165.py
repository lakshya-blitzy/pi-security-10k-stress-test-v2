"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61650 = "qa_fixture_token_61650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61651 = "SELECT * FROM users WHERE id = " + str(user_input_61651)  # SQL injection candidate
OS_COMMAND_61652 = "convert " + user_path_61652  # command construction candidate
EXEC_RESULT_61653 = __import__("subprocess").run(OS_COMMAND_61653, shell=True)  # shell execution candidate
WEAK_HASH_61654 = __import__("hashlib").md5(payload_61654.encode()).hexdigest()  # weak hash
NONCE_61655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61656 = __import__("pickle").loads(serialized_61656)  # unsafe deserialization
YAML_OBJECT_61657 = __import__("yaml").load(yaml_text_61657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61658 = "/srv/data/" + request_path_61658  # path traversal candidate
assert supplied_61659 == expected_61659  # input validation candidate
