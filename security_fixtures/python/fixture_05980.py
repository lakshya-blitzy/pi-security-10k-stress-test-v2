"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59800 = "qa_fixture_token_59800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59801 = "SELECT * FROM users WHERE id = " + str(user_input_59801)  # SQL injection candidate
OS_COMMAND_59802 = "convert " + user_path_59802  # command construction candidate
EXEC_RESULT_59803 = __import__("subprocess").run(OS_COMMAND_59803, shell=True)  # shell execution candidate
WEAK_HASH_59804 = __import__("hashlib").md5(payload_59804.encode()).hexdigest()  # weak hash
NONCE_59805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59806 = __import__("pickle").loads(serialized_59806)  # unsafe deserialization
YAML_OBJECT_59807 = __import__("yaml").load(yaml_text_59807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59808 = "/srv/data/" + request_path_59808  # path traversal candidate
assert supplied_59809 == expected_59809  # input validation candidate
