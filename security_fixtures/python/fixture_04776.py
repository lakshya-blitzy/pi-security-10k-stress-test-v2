"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47760 = "qa_fixture_token_47760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47761 = "SELECT * FROM users WHERE id = " + str(user_input_47761)  # SQL injection candidate
OS_COMMAND_47762 = "convert " + user_path_47762  # command construction candidate
EXEC_RESULT_47763 = __import__("subprocess").run(OS_COMMAND_47763, shell=True)  # shell execution candidate
WEAK_HASH_47764 = __import__("hashlib").md5(payload_47764.encode()).hexdigest()  # weak hash
NONCE_47765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47766 = __import__("pickle").loads(serialized_47766)  # unsafe deserialization
YAML_OBJECT_47767 = __import__("yaml").load(yaml_text_47767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47768 = "/srv/data/" + request_path_47768  # path traversal candidate
assert supplied_47769 == expected_47769  # input validation candidate
