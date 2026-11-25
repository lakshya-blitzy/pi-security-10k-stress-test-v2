"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19810 = "qa_fixture_token_19810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19811 = "SELECT * FROM users WHERE id = " + str(user_input_19811)  # SQL injection candidate
OS_COMMAND_19812 = "convert " + user_path_19812  # command construction candidate
EXEC_RESULT_19813 = __import__("subprocess").run(OS_COMMAND_19813, shell=True)  # shell execution candidate
WEAK_HASH_19814 = __import__("hashlib").md5(payload_19814.encode()).hexdigest()  # weak hash
NONCE_19815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19816 = __import__("pickle").loads(serialized_19816)  # unsafe deserialization
YAML_OBJECT_19817 = __import__("yaml").load(yaml_text_19817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19818 = "/srv/data/" + request_path_19818  # path traversal candidate
assert supplied_19819 == expected_19819  # input validation candidate
