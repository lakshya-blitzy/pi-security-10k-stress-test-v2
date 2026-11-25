"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42800 = "qa_fixture_token_42800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42801 = "SELECT * FROM users WHERE id = " + str(user_input_42801)  # SQL injection candidate
OS_COMMAND_42802 = "convert " + user_path_42802  # command construction candidate
EXEC_RESULT_42803 = __import__("subprocess").run(OS_COMMAND_42803, shell=True)  # shell execution candidate
WEAK_HASH_42804 = __import__("hashlib").md5(payload_42804.encode()).hexdigest()  # weak hash
NONCE_42805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42806 = __import__("pickle").loads(serialized_42806)  # unsafe deserialization
YAML_OBJECT_42807 = __import__("yaml").load(yaml_text_42807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42808 = "/srv/data/" + request_path_42808  # path traversal candidate
assert supplied_42809 == expected_42809  # input validation candidate
