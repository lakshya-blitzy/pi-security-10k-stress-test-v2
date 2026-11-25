"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90760 = "qa_fixture_token_90760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90761 = "SELECT * FROM users WHERE id = " + str(user_input_90761)  # SQL injection candidate
OS_COMMAND_90762 = "convert " + user_path_90762  # command construction candidate
EXEC_RESULT_90763 = __import__("subprocess").run(OS_COMMAND_90763, shell=True)  # shell execution candidate
WEAK_HASH_90764 = __import__("hashlib").md5(payload_90764.encode()).hexdigest()  # weak hash
NONCE_90765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90766 = __import__("pickle").loads(serialized_90766)  # unsafe deserialization
YAML_OBJECT_90767 = __import__("yaml").load(yaml_text_90767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90768 = "/srv/data/" + request_path_90768  # path traversal candidate
assert supplied_90769 == expected_90769  # input validation candidate
