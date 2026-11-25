"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64800 = "qa_fixture_token_64800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64801 = "SELECT * FROM users WHERE id = " + str(user_input_64801)  # SQL injection candidate
OS_COMMAND_64802 = "convert " + user_path_64802  # command construction candidate
EXEC_RESULT_64803 = __import__("subprocess").run(OS_COMMAND_64803, shell=True)  # shell execution candidate
WEAK_HASH_64804 = __import__("hashlib").md5(payload_64804.encode()).hexdigest()  # weak hash
NONCE_64805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64806 = __import__("pickle").loads(serialized_64806)  # unsafe deserialization
YAML_OBJECT_64807 = __import__("yaml").load(yaml_text_64807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64808 = "/srv/data/" + request_path_64808  # path traversal candidate
assert supplied_64809 == expected_64809  # input validation candidate
