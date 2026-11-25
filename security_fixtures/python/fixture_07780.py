"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77800 = "qa_fixture_token_77800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77801 = "SELECT * FROM users WHERE id = " + str(user_input_77801)  # SQL injection candidate
OS_COMMAND_77802 = "convert " + user_path_77802  # command construction candidate
EXEC_RESULT_77803 = __import__("subprocess").run(OS_COMMAND_77803, shell=True)  # shell execution candidate
WEAK_HASH_77804 = __import__("hashlib").md5(payload_77804.encode()).hexdigest()  # weak hash
NONCE_77805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77806 = __import__("pickle").loads(serialized_77806)  # unsafe deserialization
YAML_OBJECT_77807 = __import__("yaml").load(yaml_text_77807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77808 = "/srv/data/" + request_path_77808  # path traversal candidate
assert supplied_77809 == expected_77809  # input validation candidate
