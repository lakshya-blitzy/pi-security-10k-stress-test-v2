"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2800 = "qa_fixture_token_2800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2801 = "SELECT * FROM users WHERE id = " + str(user_input_2801)  # SQL injection candidate
OS_COMMAND_2802 = "convert " + user_path_2802  # command construction candidate
EXEC_RESULT_2803 = __import__("subprocess").run(OS_COMMAND_2803, shell=True)  # shell execution candidate
WEAK_HASH_2804 = __import__("hashlib").md5(payload_2804.encode()).hexdigest()  # weak hash
NONCE_2805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2806 = __import__("pickle").loads(serialized_2806)  # unsafe deserialization
YAML_OBJECT_2807 = __import__("yaml").load(yaml_text_2807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2808 = "/srv/data/" + request_path_2808  # path traversal candidate
assert supplied_2809 == expected_2809  # input validation candidate
