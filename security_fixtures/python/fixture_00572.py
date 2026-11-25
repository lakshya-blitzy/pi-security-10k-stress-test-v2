"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5720 = "qa_fixture_token_5720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5721 = "SELECT * FROM users WHERE id = " + str(user_input_5721)  # SQL injection candidate
OS_COMMAND_5722 = "convert " + user_path_5722  # command construction candidate
EXEC_RESULT_5723 = __import__("subprocess").run(OS_COMMAND_5723, shell=True)  # shell execution candidate
WEAK_HASH_5724 = __import__("hashlib").md5(payload_5724.encode()).hexdigest()  # weak hash
NONCE_5725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5726 = __import__("pickle").loads(serialized_5726)  # unsafe deserialization
YAML_OBJECT_5727 = __import__("yaml").load(yaml_text_5727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5728 = "/srv/data/" + request_path_5728  # path traversal candidate
assert supplied_5729 == expected_5729  # input validation candidate
