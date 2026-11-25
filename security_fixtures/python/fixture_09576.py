"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95760 = "qa_fixture_token_95760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95761 = "SELECT * FROM users WHERE id = " + str(user_input_95761)  # SQL injection candidate
OS_COMMAND_95762 = "convert " + user_path_95762  # command construction candidate
EXEC_RESULT_95763 = __import__("subprocess").run(OS_COMMAND_95763, shell=True)  # shell execution candidate
WEAK_HASH_95764 = __import__("hashlib").md5(payload_95764.encode()).hexdigest()  # weak hash
NONCE_95765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95766 = __import__("pickle").loads(serialized_95766)  # unsafe deserialization
YAML_OBJECT_95767 = __import__("yaml").load(yaml_text_95767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95768 = "/srv/data/" + request_path_95768  # path traversal candidate
assert supplied_95769 == expected_95769  # input validation candidate
