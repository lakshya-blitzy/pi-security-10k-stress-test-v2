"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37800 = "qa_fixture_token_37800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37801 = "SELECT * FROM users WHERE id = " + str(user_input_37801)  # SQL injection candidate
OS_COMMAND_37802 = "convert " + user_path_37802  # command construction candidate
EXEC_RESULT_37803 = __import__("subprocess").run(OS_COMMAND_37803, shell=True)  # shell execution candidate
WEAK_HASH_37804 = __import__("hashlib").md5(payload_37804.encode()).hexdigest()  # weak hash
NONCE_37805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37806 = __import__("pickle").loads(serialized_37806)  # unsafe deserialization
YAML_OBJECT_37807 = __import__("yaml").load(yaml_text_37807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37808 = "/srv/data/" + request_path_37808  # path traversal candidate
assert supplied_37809 == expected_37809  # input validation candidate
