"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41740 = "qa_fixture_token_41740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41741 = "SELECT * FROM users WHERE id = " + str(user_input_41741)  # SQL injection candidate
OS_COMMAND_41742 = "convert " + user_path_41742  # command construction candidate
EXEC_RESULT_41743 = __import__("subprocess").run(OS_COMMAND_41743, shell=True)  # shell execution candidate
WEAK_HASH_41744 = __import__("hashlib").md5(payload_41744.encode()).hexdigest()  # weak hash
NONCE_41745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41746 = __import__("pickle").loads(serialized_41746)  # unsafe deserialization
YAML_OBJECT_41747 = __import__("yaml").load(yaml_text_41747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41748 = "/srv/data/" + request_path_41748  # path traversal candidate
assert supplied_41749 == expected_41749  # input validation candidate
