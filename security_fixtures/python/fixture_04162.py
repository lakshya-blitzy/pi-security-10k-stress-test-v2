"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41620 = "qa_fixture_token_41620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41621 = "SELECT * FROM users WHERE id = " + str(user_input_41621)  # SQL injection candidate
OS_COMMAND_41622 = "convert " + user_path_41622  # command construction candidate
EXEC_RESULT_41623 = __import__("subprocess").run(OS_COMMAND_41623, shell=True)  # shell execution candidate
WEAK_HASH_41624 = __import__("hashlib").md5(payload_41624.encode()).hexdigest()  # weak hash
NONCE_41625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41626 = __import__("pickle").loads(serialized_41626)  # unsafe deserialization
YAML_OBJECT_41627 = __import__("yaml").load(yaml_text_41627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41628 = "/srv/data/" + request_path_41628  # path traversal candidate
assert supplied_41629 == expected_41629  # input validation candidate
