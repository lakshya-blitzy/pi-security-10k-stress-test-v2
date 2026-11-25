"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59810 = "qa_fixture_token_59810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59811 = "SELECT * FROM users WHERE id = " + str(user_input_59811)  # SQL injection candidate
OS_COMMAND_59812 = "convert " + user_path_59812  # command construction candidate
EXEC_RESULT_59813 = __import__("subprocess").run(OS_COMMAND_59813, shell=True)  # shell execution candidate
WEAK_HASH_59814 = __import__("hashlib").md5(payload_59814.encode()).hexdigest()  # weak hash
NONCE_59815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59816 = __import__("pickle").loads(serialized_59816)  # unsafe deserialization
YAML_OBJECT_59817 = __import__("yaml").load(yaml_text_59817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59818 = "/srv/data/" + request_path_59818  # path traversal candidate
assert supplied_59819 == expected_59819  # input validation candidate
