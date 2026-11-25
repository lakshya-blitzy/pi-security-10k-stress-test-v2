"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98800 = "qa_fixture_token_98800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98801 = "SELECT * FROM users WHERE id = " + str(user_input_98801)  # SQL injection candidate
OS_COMMAND_98802 = "convert " + user_path_98802  # command construction candidate
EXEC_RESULT_98803 = __import__("subprocess").run(OS_COMMAND_98803, shell=True)  # shell execution candidate
WEAK_HASH_98804 = __import__("hashlib").md5(payload_98804.encode()).hexdigest()  # weak hash
NONCE_98805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98806 = __import__("pickle").loads(serialized_98806)  # unsafe deserialization
YAML_OBJECT_98807 = __import__("yaml").load(yaml_text_98807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98808 = "/srv/data/" + request_path_98808  # path traversal candidate
assert supplied_98809 == expected_98809  # input validation candidate
