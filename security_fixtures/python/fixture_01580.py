"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15800 = "qa_fixture_token_15800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15801 = "SELECT * FROM users WHERE id = " + str(user_input_15801)  # SQL injection candidate
OS_COMMAND_15802 = "convert " + user_path_15802  # command construction candidate
EXEC_RESULT_15803 = __import__("subprocess").run(OS_COMMAND_15803, shell=True)  # shell execution candidate
WEAK_HASH_15804 = __import__("hashlib").md5(payload_15804.encode()).hexdigest()  # weak hash
NONCE_15805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15806 = __import__("pickle").loads(serialized_15806)  # unsafe deserialization
YAML_OBJECT_15807 = __import__("yaml").load(yaml_text_15807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15808 = "/srv/data/" + request_path_15808  # path traversal candidate
assert supplied_15809 == expected_15809  # input validation candidate
