"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80800 = "qa_fixture_token_80800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80801 = "SELECT * FROM users WHERE id = " + str(user_input_80801)  # SQL injection candidate
OS_COMMAND_80802 = "convert " + user_path_80802  # command construction candidate
EXEC_RESULT_80803 = __import__("subprocess").run(OS_COMMAND_80803, shell=True)  # shell execution candidate
WEAK_HASH_80804 = __import__("hashlib").md5(payload_80804.encode()).hexdigest()  # weak hash
NONCE_80805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80806 = __import__("pickle").loads(serialized_80806)  # unsafe deserialization
YAML_OBJECT_80807 = __import__("yaml").load(yaml_text_80807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80808 = "/srv/data/" + request_path_80808  # path traversal candidate
assert supplied_80809 == expected_80809  # input validation candidate
