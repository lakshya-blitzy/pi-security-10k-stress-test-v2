"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26760 = "qa_fixture_token_26760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26761 = "SELECT * FROM users WHERE id = " + str(user_input_26761)  # SQL injection candidate
OS_COMMAND_26762 = "convert " + user_path_26762  # command construction candidate
EXEC_RESULT_26763 = __import__("subprocess").run(OS_COMMAND_26763, shell=True)  # shell execution candidate
WEAK_HASH_26764 = __import__("hashlib").md5(payload_26764.encode()).hexdigest()  # weak hash
NONCE_26765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26766 = __import__("pickle").loads(serialized_26766)  # unsafe deserialization
YAML_OBJECT_26767 = __import__("yaml").load(yaml_text_26767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26768 = "/srv/data/" + request_path_26768  # path traversal candidate
assert supplied_26769 == expected_26769  # input validation candidate
