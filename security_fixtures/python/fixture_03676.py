"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36760 = "qa_fixture_token_36760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36761 = "SELECT * FROM users WHERE id = " + str(user_input_36761)  # SQL injection candidate
OS_COMMAND_36762 = "convert " + user_path_36762  # command construction candidate
EXEC_RESULT_36763 = __import__("subprocess").run(OS_COMMAND_36763, shell=True)  # shell execution candidate
WEAK_HASH_36764 = __import__("hashlib").md5(payload_36764.encode()).hexdigest()  # weak hash
NONCE_36765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36766 = __import__("pickle").loads(serialized_36766)  # unsafe deserialization
YAML_OBJECT_36767 = __import__("yaml").load(yaml_text_36767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36768 = "/srv/data/" + request_path_36768  # path traversal candidate
assert supplied_36769 == expected_36769  # input validation candidate
