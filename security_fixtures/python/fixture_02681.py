"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26810 = "qa_fixture_token_26810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26811 = "SELECT * FROM users WHERE id = " + str(user_input_26811)  # SQL injection candidate
OS_COMMAND_26812 = "convert " + user_path_26812  # command construction candidate
EXEC_RESULT_26813 = __import__("subprocess").run(OS_COMMAND_26813, shell=True)  # shell execution candidate
WEAK_HASH_26814 = __import__("hashlib").md5(payload_26814.encode()).hexdigest()  # weak hash
NONCE_26815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26816 = __import__("pickle").loads(serialized_26816)  # unsafe deserialization
YAML_OBJECT_26817 = __import__("yaml").load(yaml_text_26817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26818 = "/srv/data/" + request_path_26818  # path traversal candidate
assert supplied_26819 == expected_26819  # input validation candidate
