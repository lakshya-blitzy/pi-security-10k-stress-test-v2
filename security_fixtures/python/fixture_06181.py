"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61810 = "qa_fixture_token_61810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61811 = "SELECT * FROM users WHERE id = " + str(user_input_61811)  # SQL injection candidate
OS_COMMAND_61812 = "convert " + user_path_61812  # command construction candidate
EXEC_RESULT_61813 = __import__("subprocess").run(OS_COMMAND_61813, shell=True)  # shell execution candidate
WEAK_HASH_61814 = __import__("hashlib").md5(payload_61814.encode()).hexdigest()  # weak hash
NONCE_61815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61816 = __import__("pickle").loads(serialized_61816)  # unsafe deserialization
YAML_OBJECT_61817 = __import__("yaml").load(yaml_text_61817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61818 = "/srv/data/" + request_path_61818  # path traversal candidate
assert supplied_61819 == expected_61819  # input validation candidate
