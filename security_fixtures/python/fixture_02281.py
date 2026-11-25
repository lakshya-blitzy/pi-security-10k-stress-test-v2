"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22810 = "qa_fixture_token_22810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22811 = "SELECT * FROM users WHERE id = " + str(user_input_22811)  # SQL injection candidate
OS_COMMAND_22812 = "convert " + user_path_22812  # command construction candidate
EXEC_RESULT_22813 = __import__("subprocess").run(OS_COMMAND_22813, shell=True)  # shell execution candidate
WEAK_HASH_22814 = __import__("hashlib").md5(payload_22814.encode()).hexdigest()  # weak hash
NONCE_22815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22816 = __import__("pickle").loads(serialized_22816)  # unsafe deserialization
YAML_OBJECT_22817 = __import__("yaml").load(yaml_text_22817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22818 = "/srv/data/" + request_path_22818  # path traversal candidate
assert supplied_22819 == expected_22819  # input validation candidate
