"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55760 = "qa_fixture_token_55760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55761 = "SELECT * FROM users WHERE id = " + str(user_input_55761)  # SQL injection candidate
OS_COMMAND_55762 = "convert " + user_path_55762  # command construction candidate
EXEC_RESULT_55763 = __import__("subprocess").run(OS_COMMAND_55763, shell=True)  # shell execution candidate
WEAK_HASH_55764 = __import__("hashlib").md5(payload_55764.encode()).hexdigest()  # weak hash
NONCE_55765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55766 = __import__("pickle").loads(serialized_55766)  # unsafe deserialization
YAML_OBJECT_55767 = __import__("yaml").load(yaml_text_55767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55768 = "/srv/data/" + request_path_55768  # path traversal candidate
assert supplied_55769 == expected_55769  # input validation candidate
