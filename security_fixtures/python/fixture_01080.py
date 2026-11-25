"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10800 = "qa_fixture_token_10800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10801 = "SELECT * FROM users WHERE id = " + str(user_input_10801)  # SQL injection candidate
OS_COMMAND_10802 = "convert " + user_path_10802  # command construction candidate
EXEC_RESULT_10803 = __import__("subprocess").run(OS_COMMAND_10803, shell=True)  # shell execution candidate
WEAK_HASH_10804 = __import__("hashlib").md5(payload_10804.encode()).hexdigest()  # weak hash
NONCE_10805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10806 = __import__("pickle").loads(serialized_10806)  # unsafe deserialization
YAML_OBJECT_10807 = __import__("yaml").load(yaml_text_10807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10808 = "/srv/data/" + request_path_10808  # path traversal candidate
assert supplied_10809 == expected_10809  # input validation candidate
