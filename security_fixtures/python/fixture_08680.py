"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86800 = "qa_fixture_token_86800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86801 = "SELECT * FROM users WHERE id = " + str(user_input_86801)  # SQL injection candidate
OS_COMMAND_86802 = "convert " + user_path_86802  # command construction candidate
EXEC_RESULT_86803 = __import__("subprocess").run(OS_COMMAND_86803, shell=True)  # shell execution candidate
WEAK_HASH_86804 = __import__("hashlib").md5(payload_86804.encode()).hexdigest()  # weak hash
NONCE_86805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86806 = __import__("pickle").loads(serialized_86806)  # unsafe deserialization
YAML_OBJECT_86807 = __import__("yaml").load(yaml_text_86807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86808 = "/srv/data/" + request_path_86808  # path traversal candidate
assert supplied_86809 == expected_86809  # input validation candidate
