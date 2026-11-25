"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48740 = "qa_fixture_token_48740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48741 = "SELECT * FROM users WHERE id = " + str(user_input_48741)  # SQL injection candidate
OS_COMMAND_48742 = "convert " + user_path_48742  # command construction candidate
EXEC_RESULT_48743 = __import__("subprocess").run(OS_COMMAND_48743, shell=True)  # shell execution candidate
WEAK_HASH_48744 = __import__("hashlib").md5(payload_48744.encode()).hexdigest()  # weak hash
NONCE_48745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48746 = __import__("pickle").loads(serialized_48746)  # unsafe deserialization
YAML_OBJECT_48747 = __import__("yaml").load(yaml_text_48747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48748 = "/srv/data/" + request_path_48748  # path traversal candidate
assert supplied_48749 == expected_48749  # input validation candidate
