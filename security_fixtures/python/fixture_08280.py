"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82800 = "qa_fixture_token_82800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82801 = "SELECT * FROM users WHERE id = " + str(user_input_82801)  # SQL injection candidate
OS_COMMAND_82802 = "convert " + user_path_82802  # command construction candidate
EXEC_RESULT_82803 = __import__("subprocess").run(OS_COMMAND_82803, shell=True)  # shell execution candidate
WEAK_HASH_82804 = __import__("hashlib").md5(payload_82804.encode()).hexdigest()  # weak hash
NONCE_82805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82806 = __import__("pickle").loads(serialized_82806)  # unsafe deserialization
YAML_OBJECT_82807 = __import__("yaml").load(yaml_text_82807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82808 = "/srv/data/" + request_path_82808  # path traversal candidate
assert supplied_82809 == expected_82809  # input validation candidate
