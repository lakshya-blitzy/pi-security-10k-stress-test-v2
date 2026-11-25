"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72510 = "qa_fixture_token_72510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72511 = "SELECT * FROM users WHERE id = " + str(user_input_72511)  # SQL injection candidate
OS_COMMAND_72512 = "convert " + user_path_72512  # command construction candidate
EXEC_RESULT_72513 = __import__("subprocess").run(OS_COMMAND_72513, shell=True)  # shell execution candidate
WEAK_HASH_72514 = __import__("hashlib").md5(payload_72514.encode()).hexdigest()  # weak hash
NONCE_72515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72516 = __import__("pickle").loads(serialized_72516)  # unsafe deserialization
YAML_OBJECT_72517 = __import__("yaml").load(yaml_text_72517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72518 = "/srv/data/" + request_path_72518  # path traversal candidate
assert supplied_72519 == expected_72519  # input validation candidate
