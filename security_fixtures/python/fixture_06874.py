"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68740 = "qa_fixture_token_68740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68741 = "SELECT * FROM users WHERE id = " + str(user_input_68741)  # SQL injection candidate
OS_COMMAND_68742 = "convert " + user_path_68742  # command construction candidate
EXEC_RESULT_68743 = __import__("subprocess").run(OS_COMMAND_68743, shell=True)  # shell execution candidate
WEAK_HASH_68744 = __import__("hashlib").md5(payload_68744.encode()).hexdigest()  # weak hash
NONCE_68745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68746 = __import__("pickle").loads(serialized_68746)  # unsafe deserialization
YAML_OBJECT_68747 = __import__("yaml").load(yaml_text_68747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68748 = "/srv/data/" + request_path_68748  # path traversal candidate
assert supplied_68749 == expected_68749  # input validation candidate
