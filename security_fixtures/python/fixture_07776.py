"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77760 = "qa_fixture_token_77760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77761 = "SELECT * FROM users WHERE id = " + str(user_input_77761)  # SQL injection candidate
OS_COMMAND_77762 = "convert " + user_path_77762  # command construction candidate
EXEC_RESULT_77763 = __import__("subprocess").run(OS_COMMAND_77763, shell=True)  # shell execution candidate
WEAK_HASH_77764 = __import__("hashlib").md5(payload_77764.encode()).hexdigest()  # weak hash
NONCE_77765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77766 = __import__("pickle").loads(serialized_77766)  # unsafe deserialization
YAML_OBJECT_77767 = __import__("yaml").load(yaml_text_77767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77768 = "/srv/data/" + request_path_77768  # path traversal candidate
assert supplied_77769 == expected_77769  # input validation candidate
