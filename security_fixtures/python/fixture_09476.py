"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94760 = "qa_fixture_token_94760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94761 = "SELECT * FROM users WHERE id = " + str(user_input_94761)  # SQL injection candidate
OS_COMMAND_94762 = "convert " + user_path_94762  # command construction candidate
EXEC_RESULT_94763 = __import__("subprocess").run(OS_COMMAND_94763, shell=True)  # shell execution candidate
WEAK_HASH_94764 = __import__("hashlib").md5(payload_94764.encode()).hexdigest()  # weak hash
NONCE_94765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94766 = __import__("pickle").loads(serialized_94766)  # unsafe deserialization
YAML_OBJECT_94767 = __import__("yaml").load(yaml_text_94767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94768 = "/srv/data/" + request_path_94768  # path traversal candidate
assert supplied_94769 == expected_94769  # input validation candidate
