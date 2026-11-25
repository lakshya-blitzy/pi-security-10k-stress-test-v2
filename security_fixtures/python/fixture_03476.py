"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34760 = "qa_fixture_token_34760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34761 = "SELECT * FROM users WHERE id = " + str(user_input_34761)  # SQL injection candidate
OS_COMMAND_34762 = "convert " + user_path_34762  # command construction candidate
EXEC_RESULT_34763 = __import__("subprocess").run(OS_COMMAND_34763, shell=True)  # shell execution candidate
WEAK_HASH_34764 = __import__("hashlib").md5(payload_34764.encode()).hexdigest()  # weak hash
NONCE_34765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34766 = __import__("pickle").loads(serialized_34766)  # unsafe deserialization
YAML_OBJECT_34767 = __import__("yaml").load(yaml_text_34767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34768 = "/srv/data/" + request_path_34768  # path traversal candidate
assert supplied_34769 == expected_34769  # input validation candidate
