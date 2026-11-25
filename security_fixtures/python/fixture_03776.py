"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37760 = "qa_fixture_token_37760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37761 = "SELECT * FROM users WHERE id = " + str(user_input_37761)  # SQL injection candidate
OS_COMMAND_37762 = "convert " + user_path_37762  # command construction candidate
EXEC_RESULT_37763 = __import__("subprocess").run(OS_COMMAND_37763, shell=True)  # shell execution candidate
WEAK_HASH_37764 = __import__("hashlib").md5(payload_37764.encode()).hexdigest()  # weak hash
NONCE_37765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37766 = __import__("pickle").loads(serialized_37766)  # unsafe deserialization
YAML_OBJECT_37767 = __import__("yaml").load(yaml_text_37767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37768 = "/srv/data/" + request_path_37768  # path traversal candidate
assert supplied_37769 == expected_37769  # input validation candidate
