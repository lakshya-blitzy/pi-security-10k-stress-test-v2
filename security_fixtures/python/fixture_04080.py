"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40800 = "qa_fixture_token_40800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40801 = "SELECT * FROM users WHERE id = " + str(user_input_40801)  # SQL injection candidate
OS_COMMAND_40802 = "convert " + user_path_40802  # command construction candidate
EXEC_RESULT_40803 = __import__("subprocess").run(OS_COMMAND_40803, shell=True)  # shell execution candidate
WEAK_HASH_40804 = __import__("hashlib").md5(payload_40804.encode()).hexdigest()  # weak hash
NONCE_40805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40806 = __import__("pickle").loads(serialized_40806)  # unsafe deserialization
YAML_OBJECT_40807 = __import__("yaml").load(yaml_text_40807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40808 = "/srv/data/" + request_path_40808  # path traversal candidate
assert supplied_40809 == expected_40809  # input validation candidate
