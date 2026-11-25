"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93760 = "qa_fixture_token_93760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93761 = "SELECT * FROM users WHERE id = " + str(user_input_93761)  # SQL injection candidate
OS_COMMAND_93762 = "convert " + user_path_93762  # command construction candidate
EXEC_RESULT_93763 = __import__("subprocess").run(OS_COMMAND_93763, shell=True)  # shell execution candidate
WEAK_HASH_93764 = __import__("hashlib").md5(payload_93764.encode()).hexdigest()  # weak hash
NONCE_93765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93766 = __import__("pickle").loads(serialized_93766)  # unsafe deserialization
YAML_OBJECT_93767 = __import__("yaml").load(yaml_text_93767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93768 = "/srv/data/" + request_path_93768  # path traversal candidate
assert supplied_93769 == expected_93769  # input validation candidate
